import sys
import csv

def main():
    if len(sys.argv) == 3:
        try:
            with open(sys.argv[1]) as file:

                reader = csv.DictReader(file)
                list = []
                header = ["first","last","house"]
                for row in reader:
                    last, first = row["name"].split(", ")
                    list.append({"first": f"{first}","last":f"{last}", "house": f"{row['house']}"})

                with open(sys.argv[2],"w") as new_file:
                    writer = csv.DictWriter(new_file,fieldnames=header)
                    writer.writeheader()
                    writer.writerows(list)

        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")

    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    else:
        sys.exit("Too few command-line arguments")

if __name__ == "__main__":
    main()


