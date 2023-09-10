def fibonacci():
    step = 0
    stop = 1
    for sequence in range(9 + 1):
        print(step, end=", ")
        start = step + stop
        step = stop
        stop = start


fibonacci()