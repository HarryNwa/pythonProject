from time import time


def design(fn):
    print("*********************************")
    fn()
    print("*********************************")





@design
def show():
    print("How are you?")


def time_share(n):
    def wrap(*args, **kwargs):
        time_one = time()
        result = n(*args, **kwargs)
        time_two = time()
        print(f"It took {time_two - time_one}s to execute")
        return result

    return wrap

@design
@time_share
def share():
    print("\nYou're a baaaad booooy...")




