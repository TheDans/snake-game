class Robot:

    def __init__(self, name, weight, color):
        self.name = name
        self.weight = weight
        self.color = color
        


    def introduce_self(self):
        print('My name is ' + self.name)

r1 = Robot("tom", 40, "blue")

r1.introduce_self()