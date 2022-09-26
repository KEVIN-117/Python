class person:
    def __init__(self, name, job):
        self.name = name
        self.job = job
    def printData(self):
        pass


class estudent(person):
    def __init__(self, name, job, age, numberList):
        person.__init__(self, name, job)
        self.age = age
        self.numberList = numberList
    def printData(self):
        return f"Your name is {self.name} and your job is {self.job} your age is {str(self.age)} years old and your are number {str(self.numberList)} on the list"

class teacher(person):
    def __init__(self, name, job, age):
        super().__init__(name, job)
        self.age = age
    def printData(self):
        return f"Your name is {self.name} and your job is {self.job} and you have is {self.age} years old"
p1 = estudent("Kevin ", "Estudent",19,37)
print(p1.__class__)
print(p1.printData())

p2 = teacher("Alexis", "Teacher", 52)
print(p2.printData())