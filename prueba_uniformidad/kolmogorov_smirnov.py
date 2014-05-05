class KolgomorovSmirnov(object):
    """docstring for KolgomorovSmirnov"""
    def __init__(self, numeros):
        self.numeros = numeros  # cada valor r[i]
        self.n = self.numeros.__len__()
        self.d_mas   = -1
        self.d_menos = -1
        self.d       = -1
        self.start()

    def start(self):
        self.ordenar_valores()
        self.d_mas = self.calcular_d_mas()
        self.d_menos = self.calcular_d_menos()
        self.d = max(self.d_mas, self.d_menos)

    def ordenar_valores(self):
        self.numeros.sort()

    def calcular_d_mas(self):
        lista = list({})
        for i in range(0, self.n): # desde 0 hasta n-1
            print "%5.2f - %5.2f" % (((i+1.0)/self.n), self.numeros[i])
            lista.append(((i+1.0)/self.n)-self.numeros[i])
        print lista
        return max(lista)

    def calcular_d_menos(self):
        lista = list({})
        for i in range(0, self.n): # desdsde 0 hasta n-1
            print "%5.2f - %5.2f"%( self.numeros[i],((i*1.0)/self.n))
            lista.append( self.numeros[i]*1.0-((i*1.0)/self.n) ) # el algoritmo dice i-1 pero mi i comienza en 0
        print lista
        return max(lista)

    def __str__(self):
        return "n : {0:-5d}\nD+: {1:-5.2f}\nD-: {2:-5.2f}\nD : {3:-5.2f}".format(self.n,self.d_mas,self.d_menos,self.d)
if __name__ == '__main__':
    import sys,os
    ruta = os.path.join(os.path.dirname(__file__),'..')
    sys.path.append(ruta)
    from util.archivo import Archivo
    valores = Archivo('/home/ronny/archivos/libro/prueba_ks.txt').get_floats()
    ks = KolgomorovSmirnov(valores)
    print ks.numeros
    print ks
