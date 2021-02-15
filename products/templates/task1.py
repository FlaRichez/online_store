class Human: #name,age
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        print(f"{self.name} {self.age}")

class Male(Human):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.education = True

    def description(self):
        print(f"{self.name} {self.age} {self.education}")




male1 = Male(name='Abatai',age=16)
male1.description()