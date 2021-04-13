def addition(num1, num2):
    return num1 + num2


def substraction(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    return num1 / num2


operations = {
    "+": addition,
    "-": substraction,
    "*": multiplication,
    "/": division,
}


def calculator():
    num1 = float(input("Please enter the first number: \n"))
    for operation in operations:
        print(operation)
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: \n")
        num2 = float(input("Please enter the next number: \n"))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {round(answer, 3)}")
        question = input("Type 'c' if you want to continue operations on the result \n"
                         "Type 'n' if you want to start new calculation \n"
                         "Hit any key and Enter to stop.\n")
        if question == "c":
            num1 = answer
        elif question == "n":
            should_continue = False
            calculator()
        else:
            print("Thanks for using the most advanced calculator ever!")
            should_continue = False


calculator()
