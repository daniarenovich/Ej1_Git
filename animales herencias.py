class Animal:
    def __init__(self, nombre , edad , peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso

    def andar(self , pasos):
        return(f"El animal {self.nombre} ha andado {pasos} pasos")

class Perro(Animal):
    def __init__(self, nombre, edad, peso, raza):
        super().__init__(nombre, edad, peso)
        self.raza = raza

class Gato(Animal):
    def __init__(self, nombre, edad, peso, color):
        super().__init__(nombre, edad, peso)
        self.color = color

class Pajaro(Animal):
    def __init__(self, nombre, edad, peso, especie):
        super().__init__(nombre, edad, peso)
        self.especie = especie



def main():

    perro1 = Perro("Rufo", 20, 25.8, "Marrón")
    gato1 = Gato("Lorenzo", 15, 10.9, "Negro")
    pajaro1 = Pajaro("Peri", 4, 2.8, "Periquito")

    pasos = int(input("¿Cuántos pasos ha dado el animal? "))
    print(perro1.andar(pasos))


main()