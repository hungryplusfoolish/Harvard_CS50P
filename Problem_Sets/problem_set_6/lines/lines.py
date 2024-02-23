import sys

def main():

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    
    elif len(sys.argv) == 2:
        try:
            container = []
            file_name = sys.argv[1]

            if file_name[len(file_name)-3:] == ".py":
                with open(file_name) as file:
                    for line in file:
                        line = line.lstrip()
                        if line.strip() and line[0] != "#":
                            container.append(line)

                    num_of_lines = len(container)
                    print(num_of_lines)
            else:
                sys.exit("Not a Python file")
            
        except FileNotFoundError:
            sys.exit("File does not exist")
    
    else:
        sys.exit("Too few command-line arguments")

if __name__ == "__main__":
    main()