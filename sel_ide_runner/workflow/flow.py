from sel_ide_runner.workflow.instruction import Instruction, Instructions


class Workflow( object ):
    def __init__( self, instructions: Instructions, executor: Executor ):
        self.__executor = executor
        self.__instructions = instructions
        self.__inFlowStatement = None
        return

    def execute( self ):
        instr: Instruction = self.__instructions.current()
        while instr is not None and not self.__executor.isEndFlowControl( instr.Instruction, self.__inFlowStatement ):
            if self.__executor.isFlowControl( instr.Instruction ):
                self.__inFlowStatement = instr.Instruction
                wf = Workflow( self.__instructions, self.__executor )
                wf.execute()

            else:
                self.__executor.executeKeyword( instr )

            instr: Instruction = self.__instructions.next()

        return
