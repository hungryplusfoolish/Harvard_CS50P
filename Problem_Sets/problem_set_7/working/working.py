import re
import sys

#9:00 AM to 5:00 PM
#9 AM to 5 PM

def main():
    
    print(convert(input("Hours: ")))


def convert(s):
    s = s.strip()

    try:
        if time := re.search(r"^([1-9]|1[0-2])(:[0-5][0-9]) ((?:A|P)M) to ([1-9]|1[0-2])(:[0-5][0-9]) ((?:A|P)M)$",s):
            start = list(time.group(1,3))
            end = list(time.group(4,6))
            
            if "AM" in start and start[0] == "12":
                start[0] = 0
            
            if "AM" in end and end[0] == "12":
                end[0] = 0

            if "PM" in start and start[0] != "12":
                start[0] = int(start[0])+12
            
            if "PM" in end and end[0] != "12":
                end[0] = int(end[0])+12

            return f"{start[0]:>02}{time.group(2)} to {end[0]:>02}{time.group(5)}"
        

        elif time := re.search(r"^([1-9]|1[0-2]) ((?:A|P)M) to ([1-9]|1[0-2]) ((?:A|P)M)$",s):
            start = list(time.group(1,2))
            end = list(time.group(3,4))

            
            
            if "AM" in start and start[0] == "12":
                start[0] = 0
            
            if "AM" in end and end[0] == "12":
                end[0] = 0

            if "PM" in start and start[0] != "12":
                start[0] = int(start[0])+12
            
            if "PM" in end and end[0] != "12":
                end[0] = int(end[0])+12

            return f"{start[0]:>02}:00 to {end[0]:>02}:00"
        
        else:
            raise ValueError
    
    except:
        raise ValueError
        

if __name__ == "__main__":
    main()

