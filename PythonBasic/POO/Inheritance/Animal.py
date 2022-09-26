class Animal:
    def __init__(self, name, weight):
        self.__weight = weight
        self.__name = name
    def speak(self):
        pass
    def isRunning(self):
        pass


class Dog(Animal):
    Data = {}
    def __init__(self, name, color, race, weight, dateOfBirth):
        super().__init__(name, weight)
        self.__color = color
        self.__race = race
        self.__dateOfBirth = dateOfBirth
        self.Data = {"name":self.__name, "Color ":self.__color, "Race" : self.__race,
                         "Weight": self.__weight, "Birth Date" : self.__dateOfBirth}
    def printData(self):
        listKey = list(self.Data.keys())
        listValue = list(self.Data.values())
        for i in range(len(listKey)):
            print(listKey[i] +":"+ listValue[i])



tarzan = Dog("tarzan","black", "Pastor Aleman","12.5","17/12/2001")
print(tarzan.printData())