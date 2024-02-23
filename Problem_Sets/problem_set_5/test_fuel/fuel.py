def main():

   fraction = input("Fraction: ")
   print(gauge(99))

def convert(fraction):
      divider = fraction.index("/")

      x = fraction[0:divider]
      y = fraction[divider + 1:]

      if x.isnumeric() and y.isnumeric():
          if y != "0" and int(y) >= int(x):

              fraction = (int(x) / int(y))
              fraction = '{:.0f}'.format(fraction * 100)
              fraction = int(fraction)

              return fraction

          else:
              raise ZeroDivisionError
      else:
          raise ValueError



def gauge(percentage):

      percent_str = str(percentage)
      if percentage <= 10:
         return "E"
      elif 99 <= percentage <= 100:
         return "F"
      else:
         return percent_str + "%"


if __name__ == "__main__":
   main()






      
         
