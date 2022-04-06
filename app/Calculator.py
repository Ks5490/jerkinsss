def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def multi(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

def mod(num1, num2):
    return num1 % num2


def get_number(order):
    while True:
        number_str = input(f"What is the {order} number: ")
        try:
            x = float(number_str)
            return x
        except ValueError:
            print("You must enter a number")


if __name__ == '__main__':

    ans_temp = "a"
    while True:

        if ans_temp == "a":
            number1 = get_number("first")
        else:
            number1 = ans_temp

        number2 = get_number("second")

        while True:
            operator = input("What is the mathematical operator: ")
           
            if operator == "+":
                answer = add(number1, number2)
                print(f"{number1} {operator} {number2} = {answer}")
                break

            elif operator == "-":
                answer = sub(number1, number2)
                print(f"{number1} {operator} {number2} = {answer}")
                break

            elif operator == "*":
                answer = multi(number1, number2)
                print(f"{number1} {operator} {number2} = {answer}")
                break

            elif operator == "/":
                if number2 != 0:
                    answer = div(number1, number2)
                    print(f"{number1} {operator} {number2} = {answer}")
                    break
                else:
                    print("Cannot divide by 0 choose different operator")

            elif operator == "%":
                answer = mod(number1, number2)
                print(f"{number1} {operator} {number2} = {answer}")
                break

            else:
                print('Operator needs to be "+", "-" , "*", "/", "%"')
           

            
        while True: 
            next = input("Continue, New, Exit: ")
            if next == "Exit":
                exit()
            if next == "Continue":
                ans_temp = answer
                break
            if next == "New":
                ans_temp = "a"
                break
            else:
                print("Usage: Enter [Continue] to continue mathematical operations on answer, OR Enter [New] for calculation, OR Enter [Exit] to close app")


   