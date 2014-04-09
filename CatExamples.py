class Pet():
    def __init__(self):
        self.name = ""
        self.age = 0;

    def get_name(self):
        return self.name;

    def set_name(self, new_name):
        self.name - new_name;

    def get_age(self):
        return self.age

    def set_age(self, new_age):
        if new_age >= 0:
            self.age = new_age
            -
        else:
            raise Exception("Pet age cannot be negative")

# ..has a.. (Composition)
# ..is a.. (Inheritance)

# Cat   is a    Pet
# -----------------
# sub class     super class
# derived       base
# child         parent

class Cat(Pet):
    def __init__(self)
        super().__init__()

        self.secret_name = ""
    def speak(sefl):
        print(self.age, "year(s) old", self.name, "says 'Meow!'")

class Dog(Pet):
    def __init__(self):
        super.__init__()

        def speak(self):
            print(self.age, "year(s) old", self.name, "says 'Woof!'")
            
