import logo

def add(n1,n2):
    return n1 + n2
def sub(n1,n2):
    return n1 - n2
def mul(n1,n2):
    return n1 * n2
def div(n1,n2):
    return n1/n2

operations = {"+": add,
              "-": sub,
              "*": mul,
              "/": div
}

# print(operations["*"](3,2))

def calculator():
    print(logo.art)
    should_continue = True
    num1 = float(input("What is the first number?: "))
    while should_continue:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operations: ")
        num2 = float(input("What is the next number?: "))

        answer = operations[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue with {answer} or type 'n' to start a new calculation: ")
        if choice == "y":
            num1 = answer
        else:
            should_continue = False
            print("\n" * 20)
            calculator()

calculator()        