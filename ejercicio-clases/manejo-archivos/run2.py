from paquete_archivos.miarchivo import MiArchivo, MiArchivoEscribir
from paquete_modelo.mimodelo import Persona

m = MiArchivo()
m2 = MiArchivoEscribir()

lista = m.obtener_informacion()
lista = [l.split("|") for l in lista]


lista = lista[1:]
for d in lista:
    p = Persona(d[1], d[2], d[3], d[0])
    print(p)
    m2.agregar_informacion(p)

m.cerrar_archivo()
m2.cerrar_archivo()
