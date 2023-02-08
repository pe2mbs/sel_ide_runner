


class UiVisionCommands( object ):
    def __init__(self):
        self.__COMMANDS = {
            'bring browser to foreground': self.bringBrowsertoForeground,
            'capture screenshot': self.captureScreenshot,
            'capture entire page screenshot': self.captureEntirePageScreenshot,
            'click and wait': self.clickAndWait,
            'csv read': self.csvRead,
            'csv save': self.csvSave,
            'delete all cookies': self.deleteAllCookies,
            'highlight': self.highlight,
            'prompt': self.prompt,
            'source extract': self.sourceExtract,
            'source search': self.sourceSearch,
            'refresh': self.refresh,
            'select and wait': self.selectAndWait,
            'store checked': self.storeChecked,
            'store eval': self.storeEval,
            'stored vars': self.storedVars,
            'throw error': self.throwError,
            'wait for element present': self.waitForElementPresent,
            'wait for element to load': self.waitForElementToLoad,
            'wait for page to load': self.waitForPageToLoad,
            'wait for visible': self.waitForVisible,


        }
    def answerOnNextPrompt( self ):
        """
        target:         The string to be set to the next prompt pop-up
        :return:
        """
        return

