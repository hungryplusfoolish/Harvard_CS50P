import sys
from PIL import Image
from PIL import ImageOps
import os

'''
if the user does not specify exactly two command-line arguments,
if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
if the input’s name does not have the same extension as the output’s name, or
if the specified input does not exist.
'''
def main():
    cmd = sys.argv
    valid_extension = [".jpg", ".jpeg", ".png"]

    if len(cmd) == 3:
        path_marker = "/"
        
        if path_marker in cmd[1] or path_marker in cmd[2]:
             before = os.path.splitext(cmd[2][1])
             after = os.path.splitext(cmd[2][1])

        else:
             before = cmd[1]
             after = cmd[2]

        end_one = before[-4:].lower()
        end_two = after[-4:].lower()

        if end_one not in valid_extension or end_two not in valid_extension:
            sys.exit("Invalid input")
            
        elif end_one == end_two:
            try:
                with Image.open(before) as original:
                    shirt = Image.open("shirt.png")
                    shirt_size = shirt.size
                    fit_image = ImageOps.fit(original,size = shirt_size)
                    fit_image.save("test.jpg")
                    fit_image.paste(shirt,shirt)
                    fit_image.save(after)

            except FileNotFoundError:
                sys.exit("Input does not exist")
            
        else:
                sys.exit("Input and output have different extensions")
         
    elif len(cmd) < 3:
        sys.exit("Too few command-line arguments")

    else:
        sys.exit("Too many command-line arguments")


if __name__ == "__main__":
    main()