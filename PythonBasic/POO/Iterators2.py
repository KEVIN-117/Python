class Iter:
    def __init__(self, counterIter):
        self.counterIter = counterIter
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if(self.a <= self.counterIter):
            x = self.a
            self.a += 1
            return x
        else:
            return StopIteration

I = Iter(20)
iterar = iter(I)

for i in range(20):
    print(i)