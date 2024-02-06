def main():

   print(percent())
   


def percent():
   while True:
      tank = input("Fraction: ")
      try:
         divider = tank.index("/")
         x = int(tank[0:divider])
         y = int(tank[divider + 1:])
         if x > y:
            pass
         else:
            fraction = (x / y)
            if fraction <= .01 :
                return "E"
            elif .99 <= fraction <= 1:
               return "F"
            else:
               return f"{fraction:.0%}"
      except (ValueError, ZeroDivisionError):
         pass
      
main()
         
         
    
      
         
