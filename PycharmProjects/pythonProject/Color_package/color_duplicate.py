def color():
    color_box = []
    color_list1 = (["White", "Black", "Red"])
    color_list2 = (["Red", "Green"])

    for c in color_list1:
        if not c in color_list2:
            color_box = c

            print({color_box}, end="")

color()