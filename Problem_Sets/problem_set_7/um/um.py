import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    if count:= len(re.findall(r"\b(um)\b",s,flags = re.IGNORECASE)):
       return int(count)

    else:
        return 0


if __name__ == "__main__":
    main()
