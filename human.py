class Human:
    height = 180
    weight = 55

    def sleep(self, number_of_hours):
        print(self.weight * number_of_hours)
        print("yaaaaaawwwwwwwnnnnn...........i am sleeping")
        pass

    def walk(self):
        print("left foot, right foot.\nWalking is cool")
        pass


man = Human()
man.walk()
man.sleep(10)

