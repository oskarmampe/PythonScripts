import datetime

def print_header():
    print("----------------------------------------")
    print("             BIRTHDAY APP")
    print("----------------------------------------")


def get_birthday():
    print("Where were you born?")
    month = int(input("Month [MM]: "))
    day = int(input("Day [DD]: "))
    
    return datetime.date(datetime.date.today().year, month, day)


def days_between_dates(original, target):
    dt = original - target
    return dt.days 

def print_birthday(days):
    if days < 0:
        print("you had your birthday {} days ago this year".format(-days))
    elif days >0:
        print("Your birthday is in {} days!".format(days))
    else:
        print("Your birthday is today")


def main():
    print_header()
    bday = get_birthday()
    now = datetime.date.today()
    no_days = days_between_dates(bday, now)
    print_birthday(no_days)

main()
