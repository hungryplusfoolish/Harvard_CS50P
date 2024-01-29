def main():
    greeting = input("Greeting: ")
    greeting_stripped = greeting.strip()
    greeting_lower = greeting_stripped.lower()
    print(payment_calc(greeting_lower))
    
def payment_calc(greeting):
   greeting_split = greeting.split(" ")
   if greeting_split[0][:5] == "hello":
       return "$0"
   
   elif greeting[0] == "h":
       return "$20"
   
   else:
       return "$100"

            
main()




    


