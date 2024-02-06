def main ():
    print(iso_date())

def iso_date():
    count = 0

    while count < 2:
        date = input("Date: ").title()

        calendar = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
        ]

        try:
            if "/" in date:
                dash_format = date.split("/")
                month, day, year = dash_format

                if int(day) < 31 and int(month) < 12 and int(year) > 0:
                    day = day.zfill(2)
                    month = month.zfill(2)
                    return "{}-{}-{}".format(year, month, day)
                else:
                    ValueError


            elif "," in date:
                long_format = date.replace(",","").split(" ")
                month, day, year = long_format
                day = day.zfill(2)
                month = calendar.index(month) + 1
                if int(day) < 31 and month < 12 and int(year) > 0:
                    month = str(month).zfill(2)
                    return "{}-{}-{}".format(year, month, day)
                else:
                    ValueError
            else:
                ValueError

        except ValueError:
            count +=1




main()
