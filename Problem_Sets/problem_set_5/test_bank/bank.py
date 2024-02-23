def main():
    greeting = input("Greeting: ")

    print("${}".format(value(greeting)))

def value(greeting):
   greeting_stripped = greeting.strip().lower()
   greeting_split = greeting_stripped.split(" ")

   if greeting_split[0][:5] == "hello":
       return 0

   elif greeting[0] == "h":
       return 20

   else:
       return 100

if __name__ == "__main__":
    main()




    



    


