## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass
    
# Dog is-a class
class Dog(Animal):

    def __init__(self, name):
        # Dog has-a function __init__
        self.name = name
        
# Cat is-a class
class Cat(Animal):

    def __init__(self, name):
        # Cat has-a function __init__
        self.name = name
        
# Person is-a object
class Person(object):
    
    def __init__(self, name):
        # Person has-a function __init__
        self.name = name
        
        ## Person has-a pet of some kind
        self.pet = None
        
# Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        # Employee has-a salary
        self.salary = salary
        
# Fish is-a object
class Fish(object):
    pass
    
# Salmon is-a Fish
class Salmon(Fish):
    pass

# Halibut is-a fish
class Halibut(Fish):
    pass
    
    
## rover is-a Dog
rover = Dog("Rover")

# satan is-a Cat
satan = Cat("Satan")

# mary is-a Person
mary = Person("Mary")

# mary has-a pet satan
mary.pet = satan

# frank is a Employee with parameters name Frank, and salary 120000
frank = Employee("Frank", 120000)

# frank has-a pet rover
frank.pet = rover

# flipper is-a instance of Fish
flipper = Fish()

# crouse is-a instance of Salmon
crouse = Salmon()

# harry is-a instance of Halibut
harry = Halibut()