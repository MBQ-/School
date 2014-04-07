class cat():
    def __init__(self):
        self.age = 0
        self.name = ""

        def get_age(self):
            return self.age

        def set_age(self, new_age):
            if new_age >= 0:
                self.age = new_age
            else:
                false Exception()

        def get_name(self):
            return self.name

        def set_name(self, new_name):
            self.name = new_name

    def meow(self):
        print(self.age, "year old", self.name, "says meow!")
