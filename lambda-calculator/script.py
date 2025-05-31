#calculator w/lambda

operations = {
    '*': lambda x, y: x * y,  ##uses lambda instead of multiple functions for effiency sake
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '/': lambda x, y: x / y if y != 0 else print("wuutt")
}

result=0

def calc():
    global result
    x = float(input("number one\n")) ## gets user numbers
    y = float(input("number two\n")) ##
    while True:
        operation = input("operation: ")
        if operation in operations:
            result = operations[operation](x, y)
            print(result)
            continueCalc()
            break

def continueCalc():
    global result
    if input("continue(y) or restart(n)?\n").lower() == 'y':
        x = float(input("insert another number\n"))
        while True:
            operation = input("operation: ")
            if operation in operations:
                result = operations[operation](result, x)
                print(result)
                continueCalc()
                break
    else:
        calc()



calc()
