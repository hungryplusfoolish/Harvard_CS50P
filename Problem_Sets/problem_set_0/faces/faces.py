def main():
    User_Input = str(input("Please enter a series of :) or :( that you'd like me to convert to emojis (Feel free to include other words): "))
    User_Input = convert(User_Input)
    print(User_Input)

def convert(smile):
    smile = smile.replace(":)", "\U0001F642")
    smile = smile.replace(":(", "\U0001F641")
    return (smile)

main()