def main():
    name_list = []
    while True:
        try:
            name = input("Name: ")
            name_list.append(name)

        except EOFError:
            break
    
    adieu(name_list)

def adieu(name_list):
    print("Adieu, adieu, to ",end ="")

    if len(name_list) == 1:
        print(name_list[0])
    
    else:
        for i in range(len(name_list)):
            if i == len(name_list) - 1:
                print("and "+name_list[i])

            else:
                print(name_list[i]+", ",end ="")
    

main()


