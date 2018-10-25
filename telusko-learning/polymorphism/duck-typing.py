class Test:
    def __init__(self):
        print('Test initated...')

    def setup(self):
        print('Environment set')

    def execute(self, testType):
        testType.execute()

class UITest(Test):
    def __init__(self):
        Test.__init__


    def execute(self):
        print('ui test executed')

class RestTest(Test):
    def __init__(self):
        Test.__init__

    def execute(self):
        print('rest test executed')

uiTest = UITest()

restTest = RestTest()

Test.execute(restTest,uiTest)


