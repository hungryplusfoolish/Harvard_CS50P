
s = input("Plate: ")

for letter in s[:2]:
    if letter.isalpha():
        print("True")
    else:
        print("False")
        

if 2 <= len(s) <= 6:
    print("True")
    
else:
    print("False")

list = []
nums_concat = ""

if s.isalpha():
    print("Alpha: True")

else:
    for letter in s:
        list.append(letter)

    for index in range(len(list)):
        if list[index].isnumeric():
            section = list[index:]
            break
        
    for nums in section:
        nums_concat += nums
        
    if nums_concat[0] != "0" and nums_concat.isnumeric():
        print("True")
    else:
        print("False")


#def punc (s):
for char in s:
    if char.isalpha() or char.isnumeric():
        print("True")
        
    else:
        print("False")

