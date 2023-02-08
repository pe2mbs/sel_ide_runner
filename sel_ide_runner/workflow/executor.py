from sel_ide_runner.workflow.instruction import Instruction

class Executor( object ):
    def __init__( self ):
        return

    def isFlowControl( self, statement ):
        return statement in ( 'if', 'times', 'do', 'while' )

    def isEndFlowControl( self, statement, opener = None ):
        return statement == 'end'

    def executeKeyword( self, instr: Instruction ):
        return

