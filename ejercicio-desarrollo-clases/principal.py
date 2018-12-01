
from manejo import *


m = MiArchivo()
m2 = MiArchivoEscribir()


lista = m.obtener_informacion()
listaNueva = []

for linea in listaNueva:
	objeto = Estudiante(linea[0], int(linea[1]), int(linea[2]), int(linea[3]))
	m2.agregar_informacion(objeto)


m.cerrar_archivo()
m2.cerrar_archivo()



