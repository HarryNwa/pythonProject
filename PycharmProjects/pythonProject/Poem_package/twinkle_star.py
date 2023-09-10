class Poem:
    def __init__(self, line):
        self.line = line

    def lyrics(self):
        print("""Twinkle, twinkle, little star. How I wonder what you are!
        Up above the world so high, like a diamond in the sky.
        Twinkle, twinkle, little star, how I wonder what you are""")
        return f"{self.line}"


read = Poem(1)
print(read.lyrics())
