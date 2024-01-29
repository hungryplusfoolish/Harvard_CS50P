

def main():
    time = input("What time is it: ")
    military_time = convert(time)
    if 7 <= military_time <= 8:
        print("breakfast time")
    elif 12 <= military_time <= 13 :
        print("lunch time")

    elif 18 <= military_time <= 19:
        print("dinner time")
        


    

def convert(time):

    time = time.split(":")

    hour = int(time[0])
    minute = int(time[1])

    minute = minute / 60
    
    military = hour + minute
    return military


if __name__ == "__main__":
    main()
