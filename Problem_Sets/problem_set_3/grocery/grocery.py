#prompt user for items, one per line
#inputs should be case insensitive 
#end program using control-d
#ouput grocery list in different lines
#list should be in alphabetical order
#list should have the number of times inputted
#list should be in upper case

def main():
    grocery_list = []
    unique_list = []
    while True:
        try:
            item = input("").strip().upper()
            grocery_list.append(item)

        
        except EOFError:

            for item in grocery_list:
                if item not in unique_list:
                    unique_list.append(item)

            unique_list.sort()
            
            for grocery in unique_list:
             print(grocery_list.count(grocery),grocery)
            
            break

main()
            



