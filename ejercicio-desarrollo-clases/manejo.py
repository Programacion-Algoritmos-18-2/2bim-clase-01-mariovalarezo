

import codecs
class Estudiante():
	def __init__(self, nom, n1, n2, n3):
		self.nom = nom
		self.n1 = n1
		self.n2 = n2
		self.n3 = n3
		
	def obtener_nombre(self):
		return self.nom


	def obtener_promedio(self):
		self.promedio = (self.n1 + self.n2 + self.n3) / 3
		return self.promedio


class MiArchivo:
    def __init__(self):
        self.archivo = codecs.open("informacion.csv", "r")

    def obtener_informacion(self):
        return self.archivo.readlines()


    def cerrar_archivo(self):
        self.archivo.close()



class MiArchivoEscribir:
    def __init__(self):
        self.archivo = codecs.open("promedios.csv", "a")

    def agregar_informacion(self, p):
        self.archivo.write("%s tiene un promedio de: %.2f\n" % (p.obtener_nombre(), p.obtener_promedio()))

    def cerrar_archivo(self):
        self.archivo.close()




