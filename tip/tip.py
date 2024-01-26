def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
     d_trim = float(d[1:len(d)-1])
     d_format = "{:.1f}".format(d_trim)
     d_float = float(d_format)
     return d_float

def percent_to_float(p):
     p_trim = p[0:len(p)-1]
     p_float = float(p_trim)
     p_decimal = p_float / 100
     p_format = "{:.2f}".format(p_decimal)
     p_float = float(p_format)
     return p_float
main()