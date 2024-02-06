#Capture user input
twitter = input("Input: ")
container = ""
#this is an interesting way to improve the cleanliness of the code, notice this these are all lower case
vowels = ["a", "e", "i", "o", "u"] 

for letter in twitter:
    # I originally tried to do letter != vowels, but it is comparing it to the whole list and if I wanted to compare each letter I'd have to nest another loop.
    # Possible but overly complicated for this example
    if letter.lower() not in vowels:
        container += letter

print(container)   


    
    
    
