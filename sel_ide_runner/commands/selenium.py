from typing import Union, Callable, Optional


class UnknownKeyword( Exception ): pass




class SeleniumExecutor( object ):
    def __init__(self):
        self.__COMMANDS = {}
        return

    def registerKeyword( self, keyword: Union[dict,str], function: Optional[Callable] = None ):
        if isinstance( keyword, str ) and callable( function ):
            self.__COMMANDS[ self._keywordToFunction( keyword ) ] = function

        elif isinstance( keyword, dict ):
            for keyword, function in keyword.items():
                self.__COMMANDS[ self._keywordToFunction( keyword ) ] = function

        else:
            raise UnknownKeyword( 'registerKeyword unknown keyword type' )

        return

    def _keywordToFunction( self, keyword: str ):
        if ' ' not in keyword:
            return keyword

        function = ''
        space = False
        for ch in keyword:
            if ch == ' ':
                space = True
                continue

            function += ch.upper() if space else ch

        return function

    def keywordToFunction( self, keyword: str ):
        function = self._keywordToFunction( keyword )
        if function in self.__COMMANDS:
            return self.__COMMANDS[ function ]

        keyword = function.lower()
        for _keyword, function in self.__COMMANDS.items():
            if _keyword == keyword:
                return function

        raise UnknownKeyword( keyword )

    def executeKeyword( self, keyword, *args, **kwargs ):
        function = self.keywordToFunction( keyword )
        return function( *args, **kwargs )






class SeleniumIdeCommands( SeleniumExecutor ):
    def __init__(self):
        SeleniumExecutor.__init__( self )
        self.registerKeyword( {
            'add selection': self.addSelection,
            'answer on next prompt': self.answerOnNextPrompt,
            'assert': self._assert,
            'assert alert': self.assertAlert,
            'assert checked': self.assertChecked,
            'assert confirmation': self.assertConfirmation,
            'assert editable': self.assertEditable,
            'assert element present': self.assertElementPresent,
            'assert element not present': self.assertElementNotPresent,
            'assert not checked': self.assertNotChecked,
            'assert not editable': self.assertNotEditable,
            'assert not selected value': self.assertNotSelectedValue,
            'assert not text': self.assertNotText,
            'assert prompt': self.assertPrompt,
            'assert selected value': self.assertSelectedValue,
            'assert selected label': self.assertSelectedLabel,
            'assert text': self.assertText,
            'assert title': self.assertTitle,
            'assert value': self.assertValue,
            'check': self.check,
            'choose cancel on next confirmation': self.chooseCancelOnNextConfirmation,
            'choose cancel on next prompt': self.chooseCancelOnNextPrompt,
            'choose ok on next confirmation': self.chooseOkOnNextConfirmation,
            'click': self.click,
            'click at': self.clickAt,
            'close': self.close,
            'debugger': self.debugger,
            'do': self.do,
            'double click': self.doubleClick,
            'double click at': self.doubleClickAt,
            'drag and drop to object': self.dragAndDropToObject,
            'echo': self.echo,
            'edit content': self.editContent,
            'else': self._else,
            'elseif': self._elseif,
            'end': self._end,
            'execute script': self.executeScript,
            'execute async script': self.executeAsyncScript,
            'for each': self.forEach,
            'if': self._if,
            'mouse down': self.mouseDown,
            'mouse down at': self.mouseDownAt,
            'mouse move at': self.mouseMoveAt,
            'mouse out': self.mouseOut,
            'mouse over': self.mouseOver,
            'mouse up': self.mouseUp,
            'mouse up at': self.mouseUpAt,
            'open': self.open,
            'pause': self.pause,
            'remove selection': self.removeSelection,
            'repeat if': self.repeatIf,
            'run': self.run,
            'run script': self.runScript,
            'select': self.select,
            'select frame': self.selectFrame,
            'select window': self.selectWindow,
            'send keys': self.sendKeys,
            'set speed': self.setSpeed,
            'set window size': self.setWindowSize,
            'store': self.store,
            'store attribute': self.storeAttribute,
            'store json': self.storeJson,
            'store text': self.storeText,
            'store title': self.storeTitle,
            'store value': self.storeValue,
            'store window handle': self.storeWindowHandle,
            'store xpath count': self.storeXpathCount,
            'submit': self.submit,
            'times': self.times,
            'type': self._type,
            'uncheck': self.uncheck,
            'verify': self.verify,
            'verify checked': self.verifyChecked,
            'verify editable': self.verifyEditable,
            'verify element present': self.verifyElementPresent,
            'verify element not present': self.verifyElementNotPresent,
            'verify not checked': self.verifyNotChecked,
            'verify not editable': self.verifyNotEditable,
            'verify not selected value': self.verifyNotSelectedValue,
            'verify not text': self.verifyNotText,
            'verify selected label': self.verifySelectedLabel,
            'verify selected value': self.verifySelectedValue,
            'verify text': self.verifyText,
            'verify title': self.verifyTitle,
            'verify value': self.verifyValue,
            'wait for element editable': self.waitForElementEditable,
            'wait for element not editable': self.waitForElementNotEditable,
            'wait for element not present': self.waitForElementNotPresent,
            'wait for element not visible': self.waitForElementNotVisible,
            'wait for element present': self.waitForElementPresent,
            'wait for element visible': self.waitForElementVisible,
            'webdriver answer on visible prompt': self.webdriverAnswerOnVisiblePrompt,
            'webdriver choose cancel on visible confirmation': self.webdriverChooseCancelOnVisibleconfirmation,
            'webdriver choose cancel on visible prompt': self.webdriverChooseCancelOnVisiblePrompt,
            'webdriver choose ok on visible confirmation': self.webdriverChooseOkOnVisibleConfirmation,
            'while': self._while,
        } )
        return

    def addSelection( self, locator, value, *args, **kwargs ):
        """Add a selection to the set of options in a multi-select element.

        arguments
        locator: An element locator.

        value: The value to input.

        :return:
        """
        return

    def answerOnNextPrompt( self, answer, *args, **kwargs ):
        """Affects the next alert prompt. This command will send the specified answer string to it. If the alert is already present, then use "webdriver answer on visible prompt" instead.

        arguments
        answer: The answer to give in response to the prompt pop-up.

        :return:
        """
        return

    def _assert( self, variable_name, expected_value, *args, **kwargs ):
        """Check that a variable is an expected value. The variable's value will be converted to a string for comparison. The test will stop if the assert fails.

        arguments
        variable name: The name of a variable without brackets.

        expected value: The result you expect a variable to contain (e.g., true, false, or some other value).

        :return:
        """

    def assertAlert( self, alert_text, *args, **kwargs ):
        """Confirm that an alert has been rendered with the provided text. The test will stop if the assert fails.

        arguments
        alert text: text to check

        :return:
        """
        return

    def assertChecked( self, locator, *args, **kwargs ):
        """Confirm that the target element has been checked. The test will stop if the assert fails.

        arguments
        locator: An element locator.

        :return:
        """
        return

    def assertConfirmation( self, text, *args, **kwargs ):
        """Confirm that a confirmation has been rendered. The test will stop if the assert fails.

        arguments
        text: The text to use.

        :return:
        """
        return

    def assertEditable( self, locator, *args, **kwargs ):
        """Confirm that the target element is editable. The test will stop if the assert fails.

        arguments
        locator: An element locator.

        :return:
        """
        return

    def assertElementPresent( self, locator, *args, **kwargs ):
        """Confirm that the target element is present somewhere on the page. The test will stop if the assert fails.

        arguments
        locator: An element locator.

        :return:
        """
        return

    def assertElementNotPresent( self, locator, *args, **kwargs ):
        """Confirm that the target element is not present anywhere on the page. The test will stop if the assert fails.

        arguments
        locator: An element locator.

        :return:
        """
        return

    def assertNotChecked( self, locator, *args, **kwargs ):
        """Confirm that the target element has not been checked. The test will stop if the assert fails.

        arguments
        locator: An element locator.

        :return:
        """
        return

    def assertNotEditable( self, locator, *args, **kwargs ):
        """Confirm that the target element is not editable. The test will stop if the assert fails.

        arguments
        locator: An element locator.

        :return:
        """

    def assertNotSelectedValue( self, locator, text, *args, **kwargs ):
        """Confirm that the value attribute of the selected option in a dropdown element does not contain the provided value. The test will stop if the assert fails.

        arguments
        select locator: An element locator identifying a drop-down menu.

        text: An exact string match. Support for pattern matching is in the works. See https://github.com/SeleniumHQ/selenium-ide/issues/141 for details.

        :return:
        """

    def assertNotText( self, locator, text, *args, **kwargs ):
        """Confirm that the text of an element does not contain the provided value. The test will stop if the assert fails.

        arguments
        locator: An element locator.

        text: An exact string match. Support for pattern matching is in the works. See https://github.com/SeleniumHQ/selenium-ide/issues/141 for details.

        :return:
        """

    def assertPrompt( self, text, *args, **kwargs ):
        """Confirm that a JavaScript prompt has been rendered. The test will stop if the assert fails.

        arguments
        text: The text to use.

        :return:
        """

    def assertSelectedValue( self, locator, text, *args, **kwargs ):
        """Confirm that the value attribute of the selected option in a dropdown element contains the provided value. The test will stop if the assert fails.

        arguments
        select locator: An element locator identifying a drop-down menu.

        text: An exact string match. Support for pattern matching is in the works. See https://github.com/SeleniumHQ/selenium-ide/issues/141 for details.

        :return:
        """

    def assertSelectedLabel( self, locator, text, *args, **kwargs ):
        """Confirm that the label of the selected option in a dropdown element contains the provided value. The test will stop if the assert fails.

        arguments
        select locator: An element locator identifying a drop-down menu.

        text: An exact string match. Support for pattern matching is in the works. See https://github.com/SeleniumHQ/selenium-ide/issues/141 for details.

        :return:
        """

    def assertText( self, locator, text, *args, **kwargs ):
        """Confirm that the text of an element contains the provided value. The test will stop if the assert fails.

        arguments
        locator: An element locator.

        text: An exact string match. Support for pattern matching is in the works. See https://github.com/SeleniumHQ/selenium-ide/issues/141 for details.

        :return:
        """

    def assertTitle( self, text, *args, **kwargs ):
        """Confirm the title of the current page contains the provided text. The test will stop if the assert fails.

        arguments
        text: An exact string match. Support for pattern matching is in the works. See https://github.com/SeleniumHQ/selenium-ide/issues/141 for details.

        :return:
        """

    def assertValue( self, locator, text, *args, **kwargs ):
        """Confirm the (whitespace-trimmed) value of an input field (or anything else with a value parameter). For checkbox/radio elements, the value will be "on" or "off" depending on whether the element is checked or not. The test will stop if the assert fails.

        arguments
        locator: An element locator.

        text: An exact string match. Support for pattern matching is in the works. See https://github.com/SeleniumHQ/selenium-ide/issues/141 for details.

        :return:
        """

    def check( self, locator, *args, **kwargs ):
        """Check a toggle-button (checkbox/radio).

        arguments
        locator: An element locator.

        :return:
        """

    def chooseCancelOnNextConfirmation( self, *args, **kwargs ):
        """Affects the next confirmation alert. This command will cancel it. If the alert is already present, then use "webdriver choose cancel on visible confirmation" instead.

        :return:
        """

    def chooseCancelOnNextPrompt( self, *args, **kwargs ):
        """Affects the next alert prompt. This command will cancel it. If the alert is already present, then use "webdriver choose cancel on visible prompt" instead.

        :return:
        """

    def chooseOkOnNextConfirmation( self, *args, **kwargs ):
        """Affects the next confirmation alert. This command will accept it. If the alert is already present, then use "webdriver choose ok on visible confirmation" instead.


        :return:
        """

    def click( self, locator, *args, **kwargs ):
        """Clicks on a target element (e.g., a link, button, checkbox, or radio button).

        arguments
        locator: An element locator.

        :return:
        """

    def clickAt( self, locator, coord, *args, **kwargs ):
        """Clicks on a target element (e.g., a link, button, checkbox, or radio button). The coordinates are relative to the target element (e.g., 0,0 is the top left corner of the element) and are mostly used to check effects that relay on them, for example the material ripple effect.

        arguments
        locator: An element locator.

        coord string: Specifies the x,y position (e.g., - 10,20) of the mouse event relative to the element found from a locator.

        :return:
        """

    def close( self, *args, **kwargs ):
        """Closes the current window. There is no need to close the initial window, IDE will re-use it; closing it may cause a performance penalty on the test.



        :return:
        """

    def debugger( self, *args, **kwargs ):
        """Breaks the execution and enters debugger

        :return:
        """

    def do( self, *args, **kwargs ):
        """Create a loop that executes the proceeding commands at least once. Terminate the branch with the repeat if command.

        :return:
        """

    def doubleClick( self, locator, *args, **kwargs ):
        """Double clicks on an element (e.g., a link, button, checkbox, or radio button).

        arguments
        locator: An element locator.

        :return:
        """

    def doubleClickAt( self, locator, coord, *args, **kwargs ):
        """Double clicks on a target element (e.g., a link, button, checkbox, or radio button). The coordinates are relative to the target element (e.g., 0,0 is the top left corner of the element) and are mostly used to check effects that relay on them, for example the material ripple effect.

        arguments
        locator: An element locator.

        coord string: Specifies the x,y position (e.g., - 10,20) of the mouse event relative to the element found from a locator.

        :return:
        """

    def dragAndDropToObject( self, locator_src, locator_dst, *args, **kwargs ):
        """Drags an element and drops it on another element.

        arguments
        locator of object to be dragged: The locator of element to be dragged.
        locator of drag destination object: The locator of an element whose location (e.g., the center-most pixel within it) will be the point where locator of object to be dragged is dropped.

        :return:
        """

    def echo( self, message, *args, **kwargs ):
        """Prints the specified message into the third table cell in your Selenese tables. Useful for debugging.

        arguments
        message: The message to print.

        :return:
        """

    def editContent( self, locator, value, *args, **kwargs ):
        """Sets the value of a content editable element as if you typed in it.

        arguments
        locator: An element locator.
        value: The value to input.

        :return:
        """

    def _else( self, *args, **kwargs ):
        """Part of an if block. Execute the commands in this branch when an if and/or else if condition are not met. Terminate the branch with the end command.

        :return:
        """

    def _elseif( self, expression, *args, **kwargs ):
        """Part of an if block. Execute the commands in this branch when an if condition has not been met. Terminate the branch with the end command.

        arguments
        conditional expression: JavaScript expression that returns a boolean result for use in control flow commands.

        :return:
        """

    def _end( self, *args, **kwargs ):
        """Terminates a control flow block for if, while, and times.

        :return:
        """

    def executeScript( self, script, variable, *args, **kwargs ):
        """Executes a snippet of JavaScript in the context of the currently selected frame or window. The script fragment will be executed as the body of an anonymous function. To store the return value, use the 'return' keyword and provide a variable name in the value input field.

        arguments
        script: The JavaScript snippet to run.

        variable name: The name of a variable without brackets.

        :return:
        """

    def executeAsyncScript( self, script, variable, *args, **kwargs ):
        """Executes an async snippet of JavaScript in the context of the currently selected frame or window. The script fragment will be executed as the body of an anonymous function and must return a Promise. The Promise result will be saved on the variable if you use the 'return' keyword.

        arguments
        script: The JavaScript snippet to run.

        variable name: The name of a variable without brackets.

        :return:
        """

    def forEach( self, array, iterator, *args, **kwargs ):
        """Create a loop that executes the proceeding commands for each item in a given collection.

        arguments
        array variable name: The name of a variable containing a JavaScript array.

        iterator variable name: The name of the variable used when iterating over a collection in a looping control flow command (e.g., for each).

        :return:
        """

    def _if( self, expression, *args, **kwargs ):
        """Create a conditional branch in your test. Terminate the branch with the end command.

        arguments
        conditional expression: JavaScript expression that returns a boolean result for use in control flow commands.

        :return:
        """


    def mouseDown( self, locator, *args, **kwargs ):
        """Simulates a user pressing the left mouse button (without releasing it yet).

        arguments
        locator: An element locator.

        :return:
        """

    def mouseDownAt( self, locator, coord, *args, **kwargs ):
        """Simulates a user pressing the left mouse button (without releasing it yet) at the specified location.

        arguments
        locator: An element locator.

        coord string: Specifies the x,y position (e.g., - 10,20) of the mouse event relative to the element found from a locator.

        :return:
        """

    def mouseMoveAt( self, locator, coord, *args, **kwargs ):
        """Simulates a user pressing the mouse button (without releasing it yet) on the specified element.

        arguments
        locator: An element locator.

        coord string: Specifies the x,y position (e.g., - 10,20) of the mouse event relative to the element found from a locator.

        :return:
        """

    def mouseOut( self, locator, *args, **kwargs ):
        """Simulates a user moving the mouse pointer away from the specified element.

        arguments
        locator: An element locator.

        :return:
        """

    def mouseOver( self, locator, *args, **kwargs ):
        """Simulates a user hovering a mouse over the specified element.

        arguments
        locator: An element locator.

        :return:
        """

    def mouseUp( self, locator, *args, **kwargs ):
        """Simulates the event that occurs when the user releases the mouse button (e.g., stops holding the button down).

        arguments
        locator: An element locator.

        :return:
        """

    def mouseUpAt( self, locator, coord, *args, **kwargs ):
        """Simulates the event that occurs when the user releases the mouse button (e.g., stops holding the button down) at the specified location.

        arguments
        locator: An element locator.

        coord string: Specifies the x,y position (e.g., - 10,20) of the mouse event relative to the element found from a locator.

        :return:
        """

    def open( self, url, *args, **kwargs ):
        """Opens a URL and waits for the page to load before proceeding. This accepts both relative and absolute URLs.

        arguments
        url: The URL to open (may be relative or absolute).

        :return:
        """

    def pause( self, wait_time, *args, **kwargs ):
        """Wait for the specified amount of time.

        arguments
        wait time: The amount of time to wait (in milliseconds).

        :return:
        """

    def removeSelection( self, locator, option, *args, **kwargs ):
        """Remove a selection from the set of selected options in a multi-select element using an option locator.

        arguments
        locator: An element locator.

        option: An option locator, typically just an option label (e.g. "John Smith").

        :return:
        """

    def repeatIf( self, *args, **kwargs ):
        """

        :return:
        """

    def run( self, test_case, *args, **kwargs ):
        """Runs a test case from the current project.

        arguments
        test case: Test case name from the project.

        :return:
        """

    def runScript( self, script, *args, **kwargs ):
        """Creates a new "script" tag in the body of the current test window, and adds the specified text into the body of the command. Beware that JS exceptions thrown in these script tags aren't managed by Selenium, so you should probably wrap your script in try/catch blocks if there is any chance that the script will throw an exception.

        arguments
        script: The JavaScript snippet to run.

        :return:
        """

    def select( self, locator, option, *args, **kwargs ):
        """Select an element from a drop-down menu using an option locator. Option locators provide different ways of specifying a select element (e.g., label=, value=, id=, index=). If no option locator prefix is provided, a match on the label will be attempted.

        arguments
        select locator: An element locator identifying a drop-down menu.

        option: An option locator, typically just an option label (e.g. "John Smith").

        :return:
        """

    def selectFrame( self, locator, *args, **kwargs ):
        """Selects a frame within the current window. You can select a frame by its 0-based index number (e.g., select the first frame with "index=0", or the third frame with "index=2"). For nested frames you will need to invoke this command multiple times (once for each frame in the tree until you reach your desired frame). You can select the parent frame with "relative=parent". To return to the top of the page use "relative=top".

        arguments
        locator: An element locator.

        :return:
        """

    def selectWindow( self, window, *args, **kwargs ):
        """Selects a popup window using a window locator. Once a popup window has been selected, all commands will go to that window. Window locators use handles to select windows.

        arguments
        window handle: A handle representing a specific page (tab, or window).

        :return:
        """

    def sendKeys( self, locator, keys, *args, **kwargs ):
        """Simulates keystroke events on the specified element, as though you typed the value key-by-key. This simulates a real user typing every character in the specified string; it is also bound by the limitations of a real user, like not being able to type into a invisible or read only elements. This is useful for dynamic UI widgets (like auto-completing combo boxes) that require explicit key events. Unlike the simple "type" command, which forces the specified value into the page directly, this command will not replace the existing content.

        arguments
        locator: An element locator.

        key sequence: A sequence of keys to type, can be used to send key strokes (e.g. ${KEY_ENTER}).

        :return:
        """

    def setSpeed( self, wait_time, *args, **kwargs ):
        """Set execution speed (e.g., set the millisecond length of a delay which will follow each Selenium operation). By default, there is no such delay, e.g., the delay is 0 milliseconds. This setting is global, and will affect all test runs, until changed.

        arguments
        wait time: The amount of time to wait (in milliseconds).

        :return:
        """

    def setWindowSize( self, resolution, *args, **kwargs ):
        """Set the browser's window size, including the browser's interface.

        arguments
        resolution: Specify a window resolution using WidthxHeight. (e.g., 1280x800).

        :return:
        """

    def store( self, test, variable, *args, **kwargs ):
        """Save a target string as a variable for easy re-use.

        arguments
        text: The text to use.

        variable name: The name of a variable without brackets.

        :return:
        """

    def storeAttribute( self, locator, variable, *args, **kwargs ):
        """Gets the value of an element attribute. The value of the attribute may differ across browsers (this is the case for the "style" attribute, for example).

        arguments
        attribute locator: An element locator followed by an @ sign and then the name of the attribute, e.g. "foo@bar".

        variable name: The name of a variable without brackets.

        :return:
        """

    def storeJson( self, json_string, variable, *args, **kwargs ):
        """undefined

        arguments
        json: A string representation of a JavaScript object.

        variable name: The name of a variable without brackets.

        :return:
        """

    def storeText( self, locator, variable, *args, **kwargs ):
        """Gets the text of an element and stores it for later use. This works for any element that contains text.

        arguments
        locator: An element locator.

        variable name: The name of a variable without brackets.

        :return:
        """

    def storeTitle( self, text, variable, *args, **kwargs ):
        """Gets the title of the current page.

        arguments
        text: The text to use.

        variable name: The name of a variable without brackets.

        :return:
        """

    def storeValue( self, locator, variable, *args, **kwargs ):
        """Gets the value of element and stores it for later use. This works for any input type element.

        arguments
        locator: An element locator.

        variable name: The name of a variable without brackets.

        :return:
        """

    def storeWindowHandle( self, window, *args, **kwargs ):
        """Gets the handle of the current page.

        arguments
        window handle: A handle representing a specific page (tab, or window).

        :return:
        """

    def storeXpathCount( self, xpath, variable, *args, **kwargs ):
        """Gets the number of nodes that match the specified xpath (e.g. "//table" would give the number of tables).

        arguments
        xpath: The xpath expression to evaluate.

        variable name: The name of a variable without brackets.

        :return:
        """

    def submit( self, locator, *args, **kwargs ):
        """Submit the specified form. This is particularly useful for forms without submit buttons, e.g. single-input "Search" forms.

        arguments
        form locator: An element locator for the form you want to submit.

        :return:
        """

    def times( self, xtimes, limit, *args, **kwargs ):
        """Create a loop that executes the proceeding commands n number of times.

        arguments
        times: The number of attempts a times control flow loop will execute the commands within its block.

        loop limit: An optional argument that specifies the maximum number of times a looping control flow command can execute. This protects against infinite loops. The defaults value is set to 1000.

        :return:
        """

    def _type( self, locator, value, *args, **kwargs ):
        """Sets the value of an input field, as though you typed it in. Can also be used to set the value of combo boxes, check boxes, etc. In these cases, value should be the value of the option selected, not the visible text. Chrome only: If a file path is given it will be uploaded to the input (for type=file), NOTE: XPath locators are not supported.

        arguments
        locator: An element locator.

        value: The value to input.

        :return:
        """

    def uncheck( self, locator, *args, **kwargs ):
        """Uncheck a toggle-button (checkbox/radio).

        arguments
        locator: An element locator.

        :return:
        """

    def verify( self, variable, value, *args, **kwargs ):
        """Soft assert that a variable is an expected value. The variable's value will be converted to a string for comparison. The test will continue even if the verify fails.

        arguments
        variable name: The name of a variable without brackets.

        expected value: The result you expect a variable to contain (e.g., true, false, or some other value).

        :return:
        """

    def verifyChecked( self, locator, *args, **kwargs ):
        """Soft assert that a toggle-button (checkbox/radio) has been checked. The test will continue even if the verify fails.

        arguments
        locator: An element locator.

        :return:
        """

    def verifyEditable( self, locator, *args, **kwargs ):
        """Soft assert whether the specified input element is editable (e.g., hasn't been disabled). The test will continue even if the verify fails.

        arguments
        locator: An element locator.

        :return:
        """

    def verifyElementPresent( self, locator, *args, **kwargs ):
        """Soft assert that the specified element is somewhere on the page. The test will continue even if the verify fails.

        arguments
        locator: An element locator.

        :return:
        """

    def verifyElementNotPresent( self, locator, *args, **kwargs ):
        """Soft assert that the specified element is not somewhere on the page. The test will continue even if the verify fails.

        arguments
        locator: An element locator.

        :return:
        """

    def verifyNotChecked( self, locator, *args, **kwargs ):
        """Soft assert that a toggle-button (checkbox/radio) has not been checked. The test will continue even if the verify fails.

        arguments
        locator: An element locator.

        :return:
        """

    def verifyNotEditable( self, locator, *args, **kwargs ):
        """Soft assert whether the specified input element is not editable (e.g., hasn't been disabled). The test will continue even if the verify fails.

        arguments
        locator: An element locator.

        :return:
        """

    def verifyNotSelectedValue( self, locator, option, *args, **kwargs ):
        """Soft assert that the expected element has not been chosen in a select menu by its option attribute. The test will continue even if the verify fails.

        arguments
        select locator: An element locator identifying a drop-down menu.

        option: An option locator, typically just an option label (e.g. "John Smith").

        :return:
        """

    def verifyNotText( self, locator, text, *args, **kwargs ):
        """Soft assert the text of an element is not present. The test will continue even if the verify fails.

        arguments
        locator: An element locator.

        text: The text to use.

        :return:
        """

    def verifySelectedLabel( self, locator, text, *args, **kwargs ):
        """Soft assert the visible text for a selected option in the specified select element. The test will continue even if the verify fails.

        arguments
        select locator: An element locator identifying a drop-down menu.

        text: An exact string match. Support for pattern matching is in the works. See https://github.com/SeleniumHQ/selenium-ide/issues/141 for details.

        :return:
        """

    def verifySelectedValue( self, locator, option, *args, **kwargs ):
        """Soft assert that the expected element has been chosen in a select menu by its option attribute. The test will continue even if the verify fails.

        arguments
        select locator: An element locator identifying a drop-down menu.

        option: An option locator, typically just an option label (e.g. "John Smith").

        :return:
        """

    def verifyText( self, locator, text, *args, **kwargs ):
        """Soft assert the text of an element is present. The test will continue even if the verify fails.

        arguments
        locator: An element locator.

        text: The text to use.

        :return:
        """

    def verifyTitle( self, text, *args, **kwargs ):
        """Soft assert the title of the current page contains the provided text. The test will continue even if the verify fails.

        arguments
        text: The text to use.

        :return:
        """

    def verifyValue( self, locator, text, *args, **kwargs ):
        """Soft assert the (whitespace-trimmed) value of an input field (or anything else with a value parameter). For checkbox/radio elements, the value will be "on" or "off" depending on whether the element is checked or not. The test will continue even if the verify fails.

        arguments
        locator: An element locator.

        text: An exact string match. Support for pattern matching is in the works. See https://github.com/SeleniumHQ/selenium-ide/issues/141 for details.

        :return:
        """

    def waitForElementEditable( self, locator, wait_time, *args, **kwargs ):
        """Wait for an element to be editable.

        arguments
        locator: An element locator.

        wait time: The amount of time to wait (in milliseconds).

        :return:
        """

    def waitForElementNotEditable( self, locator, wait_time, *args, **kwargs ):
        """Wait for an element to not be editable.

        arguments
        locator: An element locator.

        wait time: The amount of time to wait (in milliseconds).

        :return:
        """

    def waitForElementNotPresent( self, locator, wait_time, *args, **kwargs ):
        """Wait for a target element to not be present on the page.

        arguments
        locator: An element locator.

        wait time: The amount of time to wait (in milliseconds).

        :return:
        """

    def waitForElementNotVisible( self, locator, wait_time, *args, **kwargs ):
        """Wait for a target element to not be visible on the page.

        arguments
        locator: An element locator.

        wait time: The amount of time to wait (in milliseconds).

        :return:
        """

    def waitForElementPresent( self, locator, wait_time, *args, **kwargs ):
        """Wait for a target element to be present on the page.

        arguments
        locator: An element locator.

        wait time: The amount of time to wait (in milliseconds).

        :return:
        """

    def waitForElementVisible( self, locator, wait_time, *args, **kwargs ):
        """Wait for a target element to be visible on the page.

        arguments
        locator: An element locator.

        wait time: The amount of time to wait (in milliseconds).

        :return:
        """

    def webdriverAnswerOnVisiblePrompt( self, answer, *args, **kwargs ):
        """Affects a currently showing alert prompt. This command instructs Selenium to provide the specified answer to it. If the alert has not appeared yet then use "answer on next prompt" instead.

        arguments
        answer: The answer to give in response to the prompt pop-up.

        :return:
        """

    def webdriverChooseCancelOnVisibleconfirmation( self, *args, **kwargs ):
        """Affects a currently showing confirmation alert. This command instructs Selenium to cancel it. If the alert has not appeared yet then use "choose cancel on next confirmation" instead.

        :return:
        """

    def webdriverChooseCancelOnVisiblePrompt( self, *args, **kwargs ):
        """Affects a currently showing alert prompt. This command instructs Selenium to cancel it. If the alert has not appeared yet then use "choose cancel on next prompt" instead.

        :return:
        """

    def webdriverChooseOkOnVisibleConfirmation( self, *args, **kwargs ):
        """Affects a currently showing confirmation alert. This command instructs Selenium to accept it. If the alert has not appeared yet then use "choose ok on next confirmation" instead.

        :return:
        """

    def _while( self, expression, limit, *args, **kwargs ):
        """Create a loop that executes the proceeding commands repeatedly for as long as the provided conditional expression is true.

        arguments

        conditional expression: JavaScript expression that returns a boolean result for use in control flow commands.

        loop limit: An optional argument that specifies the maximum number of times a looping control flow command can execute. This protects against infinite loops. The defaults value is set to 1000.

        :return:
        """
