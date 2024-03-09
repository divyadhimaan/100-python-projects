from art import logo

print(logo)

def add(num1,num2):
    return num1 + num2
def subtract(num1,num2):
    return num1-num2
def divide(num1,num2):
    return num1/num2
def multiply(num1,num2):
    return num1*num2;

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


result = 0
def calculator():
    num1 = float(input("What's the first Number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True
    
    while should_continue:
        operation = input("Pick an operation from above: ")
        if(operation != "+" and operation != "-" and operation != "*" and operation != "/"):
            print("Error: Not a valid operation")
            continue
        num2 = float(input("What's the next Number?: "))
        calc_func = operations[operation]
        result = calc_func(num1,num2)
        
        print(f"{num1} {operation} {num2} = {result}")

        continue_calc = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation or 'e' to exit: ")
        if continue_calc == "y":
            num1 = result
        if continue_calc == "n":
            should_continue = False
            calculator()
        if continue_calc == 'e':
            print("Goodbye geeks!")
            return

calculator()