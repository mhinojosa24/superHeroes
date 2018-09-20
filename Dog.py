class Animal:
    def __init__(self, name, sleep_duration):
        self.name = name
        self.sleep_duration = sleep_duration

    def sleep(self):
        print("{} sleeps for {} hours".format(self.name, self.sleep_duration))

class Dog(Animal):
    def bark(self):
        print("woof!")

if __name__ == "__main__":
    mydog = Dog("Mia", 1)
    mydog.sleep()
    mydog.bark()
