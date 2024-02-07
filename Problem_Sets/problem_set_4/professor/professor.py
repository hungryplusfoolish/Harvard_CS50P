import random

def main():
    total_count = 0
    correct_count = 0
    level = get_level()
    
    while total_count < 10:
        X, Y = generate_integer(level)
        answer = X + Y
        guess = 0
        chance_count = 0


        while chance_count < 3 and guess != answer:

            try:
                calc = int(input("Question #{} {} + {} = ".format(total_count + 1,X,Y)))
                if calc != answer:
                    print("EEE")
                    chance_count += 1
                else:
                    correct_count +=1
                    break
            except ValueError:
                print("EEE")
                chance_count += 1
            
            if chance_count == 3:
                print("{} + {} = {}".format(X,Y,X+Y))
        
        total_count +=1
    print("Score: ", total_count - correct_count)
    

def get_level():
    level = 0

    while level not in [1,2,3]:
        level = int(input("Level: "))
    
    return level

def generate_integer(level):
    if level in [1,2,3]:
        X = ""
        Y = ""
        for digit in range(level):
            X += str(random.randint(1,9))
            Y += str(random.randint(1,9))
            
        return int(X),int(Y)
    else:
        ValueError

if __name__ == "__main__":
    main()