class Zona:

    def __init__(self, nombre, zoo = None, animales = None):
        self._nombre = nombre
        self._zoo = zoo
        if animales is None:
            self._animales == list()
        else:
            self._animales = animales

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getZoo(self):
        return self._zoo

    def setZoo(self, zoo):
        self._zoo = zoo

    def getAnimales(self):
        return self._animales

    def setAnimales(self, animales):
        self._animales = animales

    def agregarAnimales(self, animal):
        self._animales.append(animal)

    def cantidadAnimales(self):
        return len(self._animales)

