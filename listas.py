colores = ["blanco","negro","azul marino"]

for colorin in colores:
    print(colorin)

print("colores[0]:",colores[0])

colores[0] = "Amarillo"
print(f"colores:",colores)

colores.append("Rojo")
print(f"colores:",colores)

color = input("Dime un color a agregar:")

coloresMin= [i.lower for i in colores]

try:
    pos = colores.index(coloresMin)
    print(f"{color} está en la lista, en la posición {pos}")
except Exception as e:
    print(f"{color} no está en la lista")

color.insert(2,"Magenta")
