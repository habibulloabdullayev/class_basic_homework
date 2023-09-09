#Create an object named "p1" whose name is "Anvar"
#Create an object named "p2" whose name is "Shavkat"
#Create an object named "p3" whose name is "Jasur"
class Person:
    def __init__(self,p1,p2,p3):
        self.name1 = p1
        self.name2 = p2
        self.name3 = p3
x = Person('Anvar','Shavkat','Jasur').name1
x1 = Person('Anvar','Shavkat','Jasur').name2
x2 = Person('Anvar','Shavkat','Jasur').name3
persons = []
persons.append(x)
persons.append(x1)
persons.append(x2)
print(persons)
#Add these objects to the "persons" named list