import time


def date_and_time():

    date = time.strftime("%a, %d %b %Y %H:%M:%S")
    print("Current date and time: ", date)


date_and_time()