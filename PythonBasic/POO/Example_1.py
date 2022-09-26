class Data:
    def __init__(self, name, lastName, birth):
        self.name = name
        self.lastName = lastName
        self.birth = birth


    @property
    def printDate(self):
        print(f"Hello :)\nmy name is {self.name}\nMy last name is {self.lastName}\nMy birth is {self.birth}")
    @staticmethod
    def set(self):
        pass



user_1 = Data("kevin", "Rodriguez", "17/12/2001")

user_1.printDate