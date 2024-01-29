def main():
    expression = input("Expression: ")
    (x,y,z) = expression.split(" ")
    print(f"{calculator(x,y,z):.1f}")

def calculator(first,operator,second):

    first = float(first)
    second = float(second)

    match operator:
        case "+":
            return first + second
        case "-":
            return first - second
        case "*":
            return first * second
        case "/":
            return first / second

main()