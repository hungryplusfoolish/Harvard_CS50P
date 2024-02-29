import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    ip = ip.strip()
    if ip := re.search(r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$",ip):
        container = ip.group().split(".")
        for section in container:
            if len(section) == 3:
                if int(section) > 255:
                    return False

        return True
    
    else:
        return False


if __name__ == "__main__":
    main()
