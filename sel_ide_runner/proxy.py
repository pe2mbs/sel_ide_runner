from typing import Union
import validators
import socket
from urllib.parse import urlparse
from validators.utils import validator
try:
    from pypac import PACSession, get_pac

except ( ModuleNotFoundError, ImportError ):
    pass

try:
    from requestssocks import Session as ReqSession

except ( ModuleNotFoundError, ImportError ):
    from  requests import Session as ReqSession


@validator
def validate_hostaddress( hostaddress: str ) -> bool :
    if ':' in hostaddress:
        try:
            hostaddress, port = hostaddress.split( ':' )
            if not validators.between( port, 1, 0xFFFF ):
                return False

            if validators.ipv4( hostaddress ):
                return True

            return validators.ipv4( socket.gethostbyname( hostaddress ) )

        except ValueError:
            # is IPv6 ???
            if hostaddress.startswith('['):
                hostaddress, port = hostaddress[1:].split(']')
                if not validators.between( port, 1, 0xFFFF ):
                    return False

            return validators.ipv6( hostaddress )

    return validators.ipv4( hostaddress )


class InvalidProxyConfig( Exception ): pass
class HostAddressNotValid( Exception ): pass

class Proxy( object ):
    def __init__( self, proxy_type: str = 'direct', options: Union[str,dict, None] = None ):
        """

        :param proxy_type:      string with the type of proxy 'system', 'direct', 'pac', 'manual', 'socks', 'direct'
        :param options:         string or dict with the proxy settings
                                {
                                    'http': "address'
                                    'https': "address'
                                }
        """
        self.__type = None
        self.__options = None
        self.__bypass   = []
        if proxy_type in ( 'direct', 'system' ):
            self.__type = proxy_type

        elif proxy_type == 'pac':
            if isinstance( options, str ):
                result = validate_hostaddress( options )
                if result:
                    self.__options = get_pac( url = options )
                    self.__type = proxy_type

                else:
                    raise InvalidProxyConfig( 'A proxy autoconfig URL seems invalid' )

            else:
                raise InvalidProxyConfig( 'A proxy autoconfig URL was not passed (e.g. options="http://localhost/pac")' )

        elif proxy_type == 'manual':
            if isinstance( options, str ):
                options = self._splitStringOptions( options )

            if isinstance( options, dict ):
                def verifyAndAdd( opts, key, target ):
                    url = opts.get( key )
                    if isinstance( url, str ):
                        result = validators.url( options )
                        if result:
                            target.update( { key: url } )
                            return True

                    return False

                if options.get( 'bypass' ):
                    self.__type = 'direct'
                    self.__options = None

                else:
                    self.__options = {}
                    if verifyAndAdd( options, 'http', self.__options ):
                        self.__type = proxy_type

                    if verifyAndAdd( options, 'https', self.__options ):
                        self.__type = proxy_type

                    if verifyAndAdd( options, 'ftp', self.__options ):
                        self.__type = proxy_type

                    if verifyAndAdd( options, 'socks', self.__options ):
                        self.__options[ 'version' ] = options.get( 'version' )
                        self.__type = proxy_type

                    if len( self.__options ) == 0:
                        raise InvalidProxyConfig( 'Proxy options were not passed to manual proxy (e.g. options="http=localhost:321 ftp=localhost:4324")' )

            else:
                raise InvalidProxyConfig( 'Proxy options were not passed to manual proxy (e.g. options="http=localhost:321 ftp=localhost:4324")' )

        elif proxy_type == 'socks':
            if isinstance( options, str ):
                options = self._splitStringOptions( options )

            if isinstance( options, dict ):
                if options.get( 'socks' ) is None or options.get( 'version' ) is None:
                    raise InvalidProxyConfig('Proxy socks version is invalid (e.g. options="socks=localhost:321 socksVersion=5")');

            else:
                raise InvalidProxyConfig('Proxy socks version is invalid (e.g. options="socks=localhost:321 socksVersion=5")');

            self.__type = proxy_type
            self.__options = options

        else:
            raise InvalidProxyConfig( 'An unknown proxy type was passed, use one of: direct, system, manual, socks or pac (e.g. proxy_type="direct")' )

        return

    def _splitStringOptions( self, data: str ):
        """Internal member function

        :param data:    string with attributes and values
        :return:
        """
        data = data.split( ' ' )
        if len( data ) == 1:
            data = data[ 0 ].split( ';' )

        result = {}
        for item in data:
            result.update( { key: value for key, value in item.split( '=' ) } )

        return

    def addBypass( self, hostname ):
        """This host bypass is only for a direct proxy. Whenevery using the PAC proxy configuration
        this bypassing is taken care in the PAC file.

        :param hostname:    string with hostname or IP address to bypass
        :return:            None
        """
        if validate_hostaddress( hostname ):
            self.__bypass.append( hostname )
            return

        raise HostAddressNotValid( f'{hostname} is not a valid hostname or IP address' )


    def useProxy( self ) -> bool:
        """If the proxy is set

        :return:    bool True when the proxy is configured, False for no proxy
        """
        return self.__type in ( 'pac', 'manual', 'socks' )

    @property
    def ProxyType( self ):
        """Return the proxy type

        :return:    string ( 'pac', 'manual', 'socks', 'direct' )
        """
        return self.__type

    def Session( self, url = None, proxy_auth = None ) -> ReqSession:
        """Returns a session object

        :param url:     string the requested URL, for proxy resolve
        :return:
        """
        if self.__type == 'pac':
            # Resolve via .pac file, bypasing is also in the PAC file
            return PACSession( self.__options, proxy_auth = proxy_auth )

        if isinstance( url, str ):
            r = urlparse( url )
            # First check if its a bypass hostname
            if r.hostname in self.__bypass:
                return ReqSession()

        # Just create the Session object with the proxy
        session = ReqSession( proxy_auth = proxy_auth )
        session.proxies = self.__options
        return session
