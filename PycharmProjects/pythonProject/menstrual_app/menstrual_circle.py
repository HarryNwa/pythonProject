class MenstrualCycle:
    def __init__(self, age, username, password):
        self.age = age
        self.username = username
        self.password = password

    def get_username(self):
        return self.username

    def set_username(self, username):
        self.username = username

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password
