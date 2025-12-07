class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        print(self.name, "barks!")

d = Dog("Buddy")
d.bark()