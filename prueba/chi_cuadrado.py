import math

class ChiCuadrado(object):
    """docstring for ChiCuadrado"""
    def __init__(self, valores):
        self.valores = valores
        self.n = valores.__len__()
        self.rango_menor = list({})
        self.rango_mayor = list({})
        self.fo = list({})
        print self.n
        print math.sqrt(self.n)
        print math.floor(math.sqrt(self.n))
        self.fe = int((self.n) / math.floor( math.sqrt(self.n))) # revisar
        print "self.fe",self.fe

    def start(self):
        paso = round(1.0 / self.fe,2)
        for i in range(self.fe):
            if i == 0 :
                self.rango_menor.append(0)
            else:
                self.rango_menor.append(self.rango_mayor[i-1])
            self.rango_mayor.append( self.rango_menor[i] + paso )

    def get_rango_menor(self):
        return self.rango_menor

if __name__ == "__main__":
    f = open('/home/ronny/archivos/prueba2.txt','r')
    valores = list({})
    for linea in f:
        valores.append(float(linea))
    f.close()
    print ">>",valores
    test = ChiCuadrado(valores)
    test.start()
    print test.get_rango_menor()

