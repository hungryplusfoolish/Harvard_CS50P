import sys

def main():
    print("\n")
    capacity = input("How big do you want your cookie jar to be? ",)
    jar = Jar(capacity)
    prompt = " "

    while prompt != 'Exit':
        print("\nWelcome to your cookie bank enter one of the following:\nCheck capacity ('C') | Deposit ('D') | Withdraw ('W') | Check Balance ('CB')| Change capacity ('CC')\n")
        prompt = input("What would you like to do with your cookie chart (Enter Exit to leave): ")

        match prompt:
            case "C":
                print(jar.capacity)
            case "D":
                deposit_amount = int(input(f"How many cookies would you like to deposit, your max is {jar.capacity}? "))
                jar.deposit(deposit_amount)
            case "W":
                withdrawal_amount = int(input(f"How many cookies would you like to withdraw, your max is {jar.size}? "))
                jar.withdraw(withdrawal_amount)
            case "CC":
                proposed_capacity = int(input(f"How many cookies would you like your jar to hold the max is 12? "))
                jar.capacity = proposed_capacity
            
            case "CB":
                print(f"\nYour highness, you currently have {jar.size} ({str(jar)}) cookies with a max storage capacity of {jar.capacity}.")

            case "Exit":
                sys.exit("It was a pleasure, have a nice day!\n")

#-----------------------------------------
class Jar:
    def __init__(self, capacity=12):
        if not int(capacity) > 0:
            raise ValueError
        self._capacity = int(capacity)
        self._size = 0

    def __str__(self):
        return ("🍪"* self.size)

#-----------------------------------------
    def deposit(self, n):
        self.size = self._size + n

    def withdraw(self, n):
        self.size = self._size - n
#-----------------------------------------
    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self,capacity):
        if 0 <= int(capacity) <= 12:
            self._capacity = int(capacity)
        else:
            raise ValueError
#-----------------------------------------

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size = 0):
        if not 0 <= size <= self._capacity:
             raise ValueError
        self._size = size
       

#-----------------------------------------

if __name__ == "__main__":
    main()