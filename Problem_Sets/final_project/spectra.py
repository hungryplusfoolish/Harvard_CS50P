from tabulate import tabulate
import pyfiglet
import shutil
import sys
import math

terminal_width = shutil.get_terminal_size().columns

def main():
    #--------------------------------------------------------
    #Print Program Name
    program_name = "SPECTA"
    print()
    print_header(pyfiglet.figlet_format(program_name))

    #--------------------------------------------------------
    #Introduce Program purporse
    hello_world = "Hello World"
    intro = "My current abilities are to calculate your base metabolic rate, body mass index and use computer vision to measure body fat percentage."
    
    space()
    print_voice(f"{hello_world}\n\n")
    print_voice(intro)
    print_voice("(Enter 'E' to exit)")
    section_break()
    
    #--------------------------------------------------------
    #Determine users preferred units
    unit_options = tabulate({"Key": ["A","B"], "Format": ["Inches | Pounds","Centimeters | Kilograms"]},headers = "keys",tablefmt ="double_grid", stralign="center")
    print_voice("Choose a unit system: ")
    print()
    print_options(unit_options)
    space()

    unit_preference = 0


    while unit_preference not in ["A","B","E"]:
        unit_preference = input("Key: ").upper().strip()
    
    try:
        
        section_break()
        if unit_preference == "A":
            us_format = tabulate({"Input": ["Height","Neck","Waist","Weight","Age","Sex"], "Unit": ["inches","inches","inches","lbs","yrs","M|F"]},headers = "keys",tablefmt ="double_grid", stralign="center")
            print_voice("Valid Inputs")
            print_voice("**Exclude Unit**")
            print_options(us_format)
            space()
            height = float(input("Enter your height in inches: "))*2.54
            weight = float(input("Enter your weight in lbs: "))/2.205
            neck = float(input("Enter your neck measurement(in): "))*2.54
            waist = float(input("Enter your waist measurement(in): "))*2.54
            age = float(input("Please enter your age: "))
            sex = input("Please enter your gender at birth: ").upper()
            if sex not in ["M","F"]:
                raise ValueError
            hip = None
            if sex == "F":
                hip = float(input("Enter your hip measurement(in): "))*2.54
        
        elif unit_preference == "B":
            
            uk_format = tabulate({"Input": ["Height","Neck","Waist","Weight","Age","Sex"], "Unit": ["centimeters","centimeters","centimeters","kgs","yrs","M|F"]},headers = "keys",tablefmt ="double_grid", stralign="center")
            print_voice("Valid Inputs")
            print_options(uk_format)
            print_voice("**Exclude Unit**")
            space()
            height = float(input("Enter your height in cm: "))
            weight = float(input("Enter your weight in kgs: "))
            neck = float(input("Enter your neck measurement(cm): "))
            waist = float(input("Enter your waist measurement(cm): "))
            age = float(input("Please enter your age in yrs: "))
            sex = input("Please enter your gender at birth: ").upper()
            if sex not in ["M","F"]:
                raise ValueError
            hip = None
            if sex == "F":
                hip = float(input("Enter your hip measurement(cm): "))
        
        else: 
            print()
            print_voice("Have a nice day Human.")
            print()
            print_header(pyfiglet.figlet_format(f"POWERING DOWN"))
            sys.exit()

    except ValueError:
        print()
        print_voice("Invalid input, please run the program again.")
        print()
        print_header(pyfiglet.figlet_format(f"POWERING DOWN"))
        sys.exit()


    while True:
        proceed = 0
        section_break()
        print_voice("Available Algorithims")
        program_options = tabulate({"Key": ["BMI","BMR","BFP"], "Programs": ["Body Mass Index","Base Metabolic Rate", "Body Fat Percentage"]},headers = "keys",tablefmt ="double_grid", stralign="center")
        print_options(program_options)
        space()
        program = input("Key: ").upper().strip()
        proceed = "default"
        section_break()

        if program in ["BMI","BMR","BFP"]:
                
            match program:
                
                case "BMI":
                    bmi = BMI(height,weight)
                    bmi_scale = tabulate({"BMI": ["<18.5","18.5 to 24.9","25.0 to 29.9","30<"], "Category": ["Underweight","Healthy Weight", "Overweight","Obese"]},headers = "keys",tablefmt ="double_grid", stralign="center")
                    print_voice("General Guidelines")
                    print_options(bmi_scale)
                    print()
                    print_voice(bmi)

                
                case "BMR":
                    bmr = BMR(height,weight,age,sex)
                    space()
                    print_voice(bmr)
                    print_voice("This figure represents your base (maintenance) calorie rate.")

                
                case "BFP":
                    if hip is None: 
                        bfp = BFP(height,neck,waist,sex)
                        
                    else:
                        bfp = BFP(height,neck,waist,sex,hip)
                    
                    bfp_scale = tabulate({"BFP": ["<14.0%","14 to 21%","21 to 30%"], "Category": ["Essential Fat","Fit/Average","Obese"]},headers = "keys",tablefmt ="double_grid", stralign="center")
                    print_voice("We use the well researched method of estimating the fat content of a person's body developed by US Navy.")
                    print_voice("Use this table for general guidelines regarding body fat percentage (BFP).")
                    print()
                    print_voice("General Guidelines")
                    print_options(bfp_scale)
                    print()
                    print_voice(bfp)

        elif program == "E" or proceed == "N":
            space()
            print_header(pyfiglet.figlet_format(f"POWERING DOWN"))
            sys.exit()
        
        else:
            print("SOMETHING WENT WRONG")
            space()
            print_voice("Invalid input, please run the program again.")
            space()
            print_header(pyfiglet.figlet_format(f"POWERING DOWN"))
            sys.exit()
        
        section_break()
        print()

        while proceed not in ["N","Y"]:
            proceed = input("Would you like to run another metric (Y/N)?  ").strip().upper()

        if proceed == "N":
            print()
            print_header(pyfiglet.figlet_format(f"POWERING DOWN"))
            sys.exit()

#Formatting functions
    
def space():
    print('\n' *2)

def section_break():
    print()
    print(terminal_width * "=")
    print()


def print_header(text):
    lines = text.split("\n")
    print(terminal_width * "=")
    print(terminal_width * "=")
    print()
    for line in lines:
        padding = (terminal_width - len(line)) // 2
        print(" " * padding + line)
    print(terminal_width * "=")
    print(terminal_width * "=")

def print_voice(text):
    lines = text.split("\n")
    for line in lines:
        padding = (terminal_width - len(line)) // 2
        print(" " * padding + line)

def print_options(text):
    lines = text.split("\n")
    for line in lines:
        padding = (terminal_width - len(line)) // 2
        print(" " * padding + line)


def BMR(height,weight,age,sex):

    match sex:
        case "M":
                BMR = 88.362 + (13.397*weight) + (4.799 * height) - (5.677 * age)
        
    
        case "F":
                BMR = 447.593 + (9.247*weight) + (3.098 * height) - (4.330 * age)
    
    return f"You're Base Metabolic Rate is: {BMR:,.0f}/day."


def BMI(height,weight):

    height = height / 100
    BMI = (weight)/(height**2)

    return f"You're Body Mass Index is: {BMI:.2f}."


def BFP(height,neck,waist,sex,hip = None):

    try: 
    
        match sex:
            case "M":
                    BFP = 495 /(1.0324 - 0.19077 * math.log10(waist - neck) + 0.15456 * math.log10(height))-450
        
            case "F":
                    BFP = 495 /(1.29579 - 0.35004 * math.log10(waist + hip - neck) + 0.22100 * math.log10(height))-450
        
        return f"Your Body Fat Percentage is: {BFP:.0f}%."
        
       
    
    except ValueError:
        space()
        print_voice("Invalid input, please run the program again.")
        space()
        print_header(pyfiglet.figlet_format(f"POWERING DOWN"))
        sys.exit()



if __name__ == "__main__":
    main()


