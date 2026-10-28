class Bitacora:
    def __init__(self):
        self._lineas = []

    def registrar(self, texto):
        self._lineas.append(texto)

    def mostrar(self):
        for linea in self._lineas:
            print(linea)
            