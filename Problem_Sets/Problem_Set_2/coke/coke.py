def main():
    #initializing variables to initiate loop
    due = 50
    #notice I had issues with the not initializing the bank variable before using it to incremement, this is because having bank += received is essentially saying bank = bank + received, which confuses the computer
    bank = 0
    print("Amount Due:",due)

    while bank < 50:
        received = int(input("Insert coin: "))

        if received != 5 and received != 10 and received != 25 :

            print("Amount Due:",due)
        
        else:

            bank += received
            due = 50 - bank
            if bank < 50:
                print("Amount Due:",due)
            else:
                break
    print("Change Owed:", abs(due))

main()
   
