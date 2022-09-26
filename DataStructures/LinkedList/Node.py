class Node:
    def __init__(self, data):
        self.Data = data
        self.linked = None

N = int(input("Number: "))

header = Node.__init__(input())

for i in range(N):
    if(header == None):
        header = Node.__init__(input())
    else:
        temp = Node.__init__(input())
        temp.linked = header
        header = temp
aux = header
while(aux != None):
    print(aux.Data )
    aux = aux.linked
