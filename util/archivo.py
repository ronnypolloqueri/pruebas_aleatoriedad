class Archivo(object):
    """Lee un archivo y devuelve los valores que contiene"""
    def __init__(self, archivo):
        self.archivo = archivo

    def get_floats(self):
        file = open(self.archivo, 'r')
        salida = list({})
        for linea in file:
            if linea.strip() != '':
                salida.append(float(linea))
        file.close()
        return salida


