#Create a class named "Animal". The attributes of this class
#includes COLOR, FOOD, and methods RUN, EAT
class Animal(object):

    def __init__(self, color, food):
        self.COLOR = color
        self.FOOD = food

    #RUN and EAT methods
    def RUN(self):
        print("An animal is running!")

    def EAT(self):
        print("An animal is eating " + self.FOOD + "!\n")

#Dog is a subclass of Animal, it has one more attribute AGE
#and one more method SAY_HELLO
class Dog(Animal):s
    def __init__(self, color, food, age):
        super(Dog, self).__init__(color, food)
        self.AGE = age

    def RUN(self):
        print("A dog is running!")

    def SAY_HELLO(self):
        age = raw_input('What is the age? ')
        print("I am a " + age + " years old dog! How are you?\n")


class Poodle(Dog):
    def __init__(self, color, food, age):
        super(Poodle, self).__init__(color, food, age)

    def RUN(self):
        print("A poodle is running!")

    def SAY_BYE(self):
        print("BYE-BYE, my homework is done!\n")


# driver code to test above classes

# Animal class
animal = Animal("", "meat")
animal.RUN()
animal.EAT()

# Dog class
dog = Dog("", "", 5 )
dog.RUN()
dog.SAY_HELLO()

# Poodle class
poodle = Poodle("", "", 5)
poodle.RUN()
poodle.SAY_BYE()