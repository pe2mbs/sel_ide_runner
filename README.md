# Selenium IDE Runner
This package can exeecute Selenium-IDE scripts from Python.

This package was build to integrate into an automation platform, to fully utilize the Selenium IDE in created the test 
scripts.

The mail goal was to keep the package as simple a posible. Therefore the SeleniumLibrary of RobotFramewak is 
used to execute the the Selenium IDE commands. SeleniumLibrary is a well maintains package and why inventing 
the wheel again.  

## Version 1.0.0
This version supports all the commands towards Selenium. 
Flow control is not yet supported. And storing variables is minimal supported. Upon executing an unsuported 
command de package throws an exception: NotImplemented or FlowControlNotSupported.

## Command line execution
sel-ide-runner [ <options> ] <ide.filename> [ { test <test-case-name> | suite <suite-name> } ]

Options:
-v/--verbose                        Be very verbose in the output
-h/--help                           Help page
-s/--server <url>                   The URL to the Selenium server, when omitted http://localhost:1234 is used
-l/--logfile <file>                 The the filename for the logger
-S/--screenshot <dir>               Screen shot storage folder
-D/--data <dir>                     Data storage folder 
-K/--keystore <file>                The pykeystore to be used
-P/--passphrase <file|passphrase>   The passphrase file or the actual passphrase 

