import sys

express = ' '.join(sys.argv[1:])
if len(sys.argv[1:]) < 1:
    express = input("enter calc, this way (n1 '+' n2):: ")
args = express.split(' ')
func = None

result = 0
for arg in args:
    if arg.isnumeric():
        if func == None:
            if not result:
                result = int(arg)
        else:
            result = func(result, int(arg))
            func = None
    elif arg == "+":
        func = lambda n1, n2: n1 + n2
    elif arg == "x": 
        func = lambda n1, n2: n1 * n2
    elif arg == "-":
        func = lambda n1, n2: n1 - n2
    elif arg == "/":
        func = lambda n1, n2: n1 / n2
print(result)