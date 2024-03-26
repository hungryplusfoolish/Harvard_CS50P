import sys

class Jar:
    def __init__(self,name, house, patronous):
        self.name = name
        self.house = house
        self.patronous = patronous
    
    def charm(self):
        match self.patronous:
            case "Horse":
                return "🐎"
            case "Hound":
                return "🦮"
    
    def __str__(self):
        return "You found me"
                



def get_jar():
    name = input("Name: ")
    house = input("House: ")
    patronous = input("Patronous: ")
    return Jar(name,house,patronous)


def main():
    jar = get_jar()
    print(jar)
    print(jar.charm())




    '''
    def __init__(self, count = None, capacity = 12):
        if not count:
            #sys.exit("please try again")
            raise ValueError("Missing count")
    
            self.count = count
            self.capacity = capacity

    def __str__(self):
        return (f"You currently have {self.count} cookies out of total storage for {self.capacity} cookies")

    
'''



    





class Bar:
    def __init__(self, vault=12):
        self.vault = vault

    def __str__(self):
        ...

    def deposit(self, n):
        ...

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...

if __name__ == "__main__":
    main()