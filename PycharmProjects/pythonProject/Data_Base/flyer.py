class Flyer:
    def fly(self, fly):
        fly.fly()


class Bird:
    def fly(self):
        print("flying")


class Chicken:
    def fly(self):
        print("Chicken is flying")


flyer1 = Flyer()
bird1 = Bird()
chicken1 = Chicken()

flyer1.fly(bird1)
flyer1.fly(chicken1)
