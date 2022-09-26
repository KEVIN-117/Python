class nuberIter:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x

I = nuberIter()
iterar = iter(I)
"""print(next(iterar))
print(next(iterar))
print(next(iterar))
print(next(iterar))
print(next(iterar))
print(next(iterar))
print(next(iterar))
print(next(iterar))
print(next(iterar))
print(next(iterar))
print(next(iterar))
print(next(iterar))
print(next(iterar))
print(next(iterar))
print(next(iterar))
print(next(iterar))
print(next(iterar))
print(next(iterar))
print(next(iterar))
print(next(iterar))"""
printValue = ""

for i in range(200):
    printValue += str(next(iterar))+", "
print(printValue)
