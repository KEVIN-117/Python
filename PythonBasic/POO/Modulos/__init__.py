import Animal as a
import platform

print(platform.system())
print(platform.machine())
print(platform.processor())
print(platform.python_branch())
print(platform.win32_edition())
print(platform.node())
print(platform.win32_is_iot())


perro = a.Animal("Tarzan", "Perro","4","negro", "croquetas")
print(perro.comer())
print(perro.printData())