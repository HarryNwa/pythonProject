letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"]


def list_slice(start, step):
    return [start[a::3] for a in range(step)]


print(list_slice(letters, 3))


