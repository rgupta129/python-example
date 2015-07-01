class FunctionCallInterceptor(object):
    def __init__(self, targetFunction):
        self.targetFunction = targetFunction

    def __call__(self, param):
        print "Entering-->", self.targetFunction.__name__
        self.targetFunction(param)
        print "<--Exited", self.targetFunction.__name__

# Use python decorator to intercept calls to func1 and func2
@FunctionCallInterceptor
def func1(param):
    print "inside func1(): " + str(param)

@FunctionCallInterceptor
def func2(param):
    print "inside func2(): " + str(param)

if __name__ == "__main__":
    func1("param1")
    func2("param2")
    """
        Expected output:
            Entering--> func1
            inside func1(): param1
            <--Exited func1
            Entering--> func2
            inside func2(): param2
            <--Exited func2
    """
