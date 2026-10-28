from bitacora import Bitacora

bit = Bitacora()
bit.registrar("primer evento")
bit.registrar("segundo evento")
bit.mostrar()
print("Total de eventos:", len(bit._lineas))