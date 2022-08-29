def format_date(day, month, year):
    b = ''
    months = {1: "styczen", 2: "luty", 3: "marzec", 4: "kwiecień", 5: "maj", 6: "czerwiec", 7: "lipiec",
              8: "sierpien", 9: "wrzesień", 10: "październik", 11: "listopad", 12: "grudzień"}
    if month < 13:
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12 and day < 32:
            b = "{}-{}-{}".format(day, months[month], year)
            print("data jest ok")
            return b
        if month == 2 and day < 29:
            b = "{}-{}-{}".format(day, months[month], year)
            print("data jest ok")
            return b
        if month == 4 or month == 6 or month == 9 or month == 11 and day < 31:
            b = "{}-{}-{}".format(day, months[month], year)
            print("data jest ok")
            return b


a = format_date(12, 1, 2015)
print(a)
