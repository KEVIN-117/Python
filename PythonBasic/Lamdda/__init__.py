class first:
    def __init__(self):
        pass
    def Data(self, name, age):
        print(f"My name is {name} and i am {age} years old")



date = first()

print(date.Data("Kevin", 21))
dicyt = {"name":"kehgewfw", "bdqwnd":"hyiwdqw"}
listKey = list(dicyt.keys())
listValue = list(dicyt.values())
for i in range(len(listValue)):
    print(listKey[i] , "= ", listValue[i])
print(len(dicyt))