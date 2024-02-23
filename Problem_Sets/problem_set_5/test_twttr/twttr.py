#Capture user input

def main ():
    word = input("Input: ")
    print(shorten(word))
    #this is an interesting way to improve the cleanliness of the code, notice this these are all lower case

def shorten(word):
    container = ""
    vowels = ["a", "e", "i", "o", "u"] 

    for letter in word:
        # I originally tried to do letter != vowels, but it is comparing it to the whole list and if I wanted to compare each letter I'd have to nest another loop.
        # Possible but overly complicated for this example

        if letter.lower() not in vowels:
            container += letter
        
    return str(container)

if __name__ == "__main__":
    main()
        
 


    
    
    
