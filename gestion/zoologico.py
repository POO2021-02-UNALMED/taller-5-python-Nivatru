

class Zoologico:

    def __init__(self, nombre, ubicacion, zonas = None):
        self._nombre = nombre
        self._ubicacion = ubicacion
        if zonas is None:
            self._zonas = list()
        else:
            self._zonas = zonas

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getUbicacion(self):
        return self._ubicacion

    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion

    def getZonas(self):
        return self._zonas

    def setZonas(self, zonas):
        self._zonas = zonas

    def agregarZonas(self, zona):
        self._zonas.append(zona)

    def cantidadTotalAnimales(self):
        animales = [x.cantidadAnimales() for x in self._zonas]
        return sum(animales)