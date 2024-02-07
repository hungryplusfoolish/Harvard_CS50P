import random

def main():

        upper_lvl = 0
        guess = 0
    
        while upper_lvl < 1: 
            try:
                 upper_lvl = int(input("Level: "))
            
            except ValueError:
                 pass
    
        secret = random.randint(1,upper_lvl)
    
        while guess != secret:
            try:
                guess = int(input("Guess: "))

                if guess < 0:
                    pass
                elif guess < secret:
                    print("Too small!")

                elif guess > secret:
                    print("Too large!")
                else:
                    print("Just right!")

            except ValueError:
                 pass

main()
    
    