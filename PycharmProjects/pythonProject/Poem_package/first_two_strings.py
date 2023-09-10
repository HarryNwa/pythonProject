def copies():
    lst = ["enter"]
    # word = input("Enter word: ")
    for w in lst:
        if w == lst[0]:
            print(w[0])
        elif w == lst[1]:
            print(w[1])

        print(w[0], w[1])

copies()
