class Python_version:
    def __init__(self, version):
        self.version = version

    def python(self):
        print("""PyCharm Professional Edition. 2022""")
        return f"{self.version}"


read = Python_version(1)
print(read.python())