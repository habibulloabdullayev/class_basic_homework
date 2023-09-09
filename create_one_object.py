#create an object named "person" whose name is "Ali"
class Person:
    def __init__(self,name):
        self.name = name
name_1 = Person('Ali')
print(name_1.name)