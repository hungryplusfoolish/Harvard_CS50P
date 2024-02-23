import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) == 2:
        pie_type = sys.argv[1]

        if pie_type[-4:] == ".csv":
            try:
                with open(pie_type) as file:
                    menu = []
                    for row in file:
                        row = row.rstrip().split(",")
                        menu.append(row)
                    
                    print(tabulate(menu[1:], headers = menu[0], tablefmt = "outline"))
            
            except FileNotFoundError:
                sys.exit("File does not exist")
        
        else:
            sys.exit("Not a CSV file")
    
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    else:
        sys.exit("Too few command-line arguments")


if __name__ == "__main__":
    main()