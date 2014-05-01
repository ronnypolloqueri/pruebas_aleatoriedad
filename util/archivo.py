class Archivo(object):
    """Lee un archivo y devuelve los valores que contiene"""
    def __init__(self, archivo):
        self.archivo = archivo

    def get_floats(self):
        salida = list({})
        for linea in self.archivo:
            salida.append(float(linea))
        return salida


