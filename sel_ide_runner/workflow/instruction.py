


class Instruction( object ):
    def __init__(self):
        self.__instr = None
        return

    @property
    def Instruction( self ):
        return self.__instr

class Instructions( list ):
    def __init__(self):
        list.__init__( self )
        self.__idx = 0
        return

    def current( self ):
        return self[ self.__idx ]

    def next( self ):
        self.__idx += 1
        if self.__idx >= len( self ):
            return None

        return self[ self.__idx ]

