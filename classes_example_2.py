##Animal is_a object(yes,sort of confusing)
class Animal(object):
    pass

#Is_a when you talk about nobjects and classes being related to each other by
#a class relationship

#Has_A when you talk about objects and classes that are related only becaure
#they reference each other

class Dog(Animal):

    def __init__(self,name):
        #dog has a name .
        self.name = name

#Cat is a animal
class Cat(Animal):
    def __init__(self,name):
        #cat has a name ,
        self.name = name

#person is a object
class Person(object):
    def __init__(self,name):
        #Person has a name
        self.name = name
        ##PErson Has- a pet of some kind
        self.pet = None

#empolyee is a person
class Employee(Person):
    def __init__(self, name,salary):
        super(Employee,self).__init__(name)
        #employee has a salary
        self.salary = salary

#fish is a object
class Fish(object):
    pass

#salmon is a fish
class Salmon(Fish):
    pass

#Halibut is a fish
class Halibut(Fish):
    pass

#Rover is a dog
rover = Dog("Rover")
#Satan is a cat
satan = Cat("Satan")

#Mary is a person
mary = Person("Mary")

#mary has a pet named satan
mary.pet = satan

#frank is a employee
frank = Employee("frank", 120000)

#frank has a pet named rover
frank.pet =rover

#flipper is a fish
flipper = Fish()

#crouse is a salmon
crouse = Salmon()

#harry is a Halibut
harry = Halibut()

#output pet names
print(mary.pet.name)
print(frank.pet.name)
