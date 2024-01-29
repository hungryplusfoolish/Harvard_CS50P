def main():
    answer = input("What is the Answer to the Great Question of Life, and Everything? ")
    answer = answer.lower().strip()


    match answer: 
        case "forty-two" | "forty two" | "42":
            print("Yes")
        case _:
            print("No")

main()