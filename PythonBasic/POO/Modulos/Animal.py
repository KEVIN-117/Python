class Animal:

    def __init__(self, name, type, numeroPatas, color, alimento):
        self.name = name
        self.type = type
        self.numeroPatas = numeroPatas
        self.color = color
        self.alimento = alimento
    def comer(self):
        return f"El {self.name} come {self.alimento}"
    def printData(self):
        return f"El animal pertenece al reyno animal {self.type}\nsu nombre es {self.name}\ncamina" \
               f" en {self.numeroPatas} patas\nes de color {self.color}\ncome {self.alimento}"