#Cambio cambio2 cambio3



class Arbol:
    def __init__(self):
        self.tipo = ""
        self.edad = 0
        self.lugar_plantado = ""
        self.raiz = Raiz()
        self.tronco = Tronco()
        self.copa = Copa()

    def __str__(self):
        return " Edad:" + str(self.edad) + " Altura del Tronco:" + str(self.tronco.altura)  

class Tronco:
    def __init__(self):
        self.altura = 0
        self.diamentro = 0


class Raiz:
    def __init__(self):
        self.numero_raices = 0
        self.tamanio_medio = 0.0

class Copa:
    def __init__(self):
        self.numero_ramas = 0
        self.hojas_por_rama = 0


mi_arbol = Arbol()
mi_arbol.tronco.altura = 99
print(mi_arbol.tronco)
mi_arbol.tronco = Tronco()
print(mi_arbol.tronco)
print(mi_arbol.tronco.altura)
print(mi_arbol.__str__)
