from datetime import date, timedelta
import inflect
import sys

#Five hundred twenty-five thousand, six hundred minutes
def main():
    

    p = inflect.engine()
    birth = input("Date of Birth: ")
    
    year, month, day = birth.split("-")
    raw = (date.today() - date(int(year),int(month),int(day)))
    minutes = int((raw.days() * (24*60)))
    string = p.number_to_words(minutes,andword="")
    print(f"{string} minutes".capitalize())
        
    

'''
def date_delta(birth):
    p = inflect.engine()

    try:
        year, month, day = birth.split("-")
        raw = (date.today() - date(int(year),int(month),int(day)))
        minutes = int((raw.days * (24*60)))
        return p.number_to_words(minutes,andword="")


    except ValueError:    
        raise ValueError
        
'''
if __name__ == "__main__":
    main()