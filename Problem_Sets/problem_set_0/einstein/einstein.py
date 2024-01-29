# Have user enter to enter mass and return this energy in joules
print("Hello human, I am program created to convert mass into energy.")
user_input = float(input("Please enter a figure for mass to convert into energy: "))
energy = user_input * (3*(10**8))**2
formatted_energy = "{:,.2f}".format(energy)
print(formatted_energy)