def main():
    #prompting user for input in Camel Case
    camel_case = input("Please enter the string in Camel Case: ")

    #creating some empty variables
    snake_case = ""
    letter_list = []

    #iterating through each letter in the camel_case input
    for letter_index in range(len(camel_case)):
        # checking to see if the letter is uppercase and it is not the first letter in the input
        if camel_case[letter_index].isupper() and letter_index != 0:
            #if it is uppercase and it is not the first letter then we need to include the "_"
            letter_list.append("_")
            #we then append the lower case letter to our empty list
            letter_list.append(camel_case[letter_index].lower())
        # establishing a catch all while still appending lowercase letter to empty list
        else:
            letter_list.append(camel_case[letter_index].lower())
    # reconstructing word into snakecase empty variable
    for letter in letter_list:
        snake_case = snake_case+ letter
    
    print(snake_case)

main()
         

        

