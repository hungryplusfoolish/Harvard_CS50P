def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if start(s) and length(s) and end(s) and punc(s):
        return True
    else:
        return False

def start(s):
    for letter in s[:2]:
        if letter.isalpha():
            return True
        else:
            return False

def length(s):
    if 2 <= len(s) <= 6:
        return True
    else:
        return False

def end(s):
    if s.isalpha():
        return True
    
    elif not s.isalnum():
        return False
    
    else:
        list = []
        nums_concat = ""
        for letter in s:
            list.append(letter)

        for index in range(len(list)):
            if list[index].isnumeric():
                section = list[index:]
                break

        for nums in section:
            nums_concat += nums

        if nums_concat[0] != "0" and nums_concat.isnumeric():
            return True
        else:
            return False


def punc (s):
    for char in s:
        if char.isalnum():
            return True
        else:
            return False


if __name__ == "__main__":
    main()
