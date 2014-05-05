import math

class ChiCuadrado(object):
    """docstring for ChiCuadrado"""
    def __init__(self, valores):
        self.valores = valores
        self.n = valores.__len__()
        self.m = math.sqrt(self.n)
        self.rango_menor = list({})
        self.rango_mayor = list({})
        self.fo = list({})
        self.cuadrados = list({})

        self.sum_fo = 0
        self.sum_cuadrados = 0

        print self.n
        print 'm = sqrt({0:4d}) = {1:6.2f}'.format(self.n, self.m)
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
        self.rango_mayor[i] = 1.0 # el ultimo valor debe ser 1.0
        self.iniciar_conteo()

    def iniciar_conteo(self):
        self.sum_fo = 0
        self.sum_cuadrados = 0
        for i in range(self.fe):
            if i != (self.fe - 1):
                self.fo.append( self.contar( self.rango_menor[i], self.rango_mayor[i], ">" ) )
            else:
                self.fo.append( self.contar( self.rango_menor[i], self.rango_mayor[i], "]" ) )
            self.cuadrados.append(math.pow(self.fe - self.fo[i],2)/self.fe)
            self.sum_fo += self.fo[i]
            self.sum_cuadrados += self.cuadrados[i]

    def contar(self, rango_inferior, rango_superior, llave_derecha):
        contador = 0
        for i in range(self.n):
            if llave_derecha == ">":
                if ( rango_inferior <= valores[i] ) and ( valores[i] < rango_superior ):
                    contador += 1
            elif llave_derecha == "]":
                if ( rango_inferior <= valores[i] ) and ( valores[i] <= rango_superior ):
                    contador += 1
        return contador

    def reporte(self):
        str = ' {0:2s}| {1:14s}  |  {2:3s}|  {3:3s}|        |((FE-FO^2)/FE|'
        print str.format('i','rangos','FO','FE')
        for i in range(self.fe):
            if i != (self.fe - 1 ) :
                str = '{0:2d} | [ {1:1.2f} : {2:1.2f} > | {3:3d} | {4:3d} | {5:-6.2f}/{4:d} | {7:-3.2f}'
            else :
                str = '{0:2d} | [ {1:1.2f} : {2:1.2f} ] | {3:3d} | {4:3d} | {5:-6.2f}/{6:d} | {7:-3.2f}'
            print str.format(i+1,
                                self.rango_menor[i],
                                self.rango_mayor[i],
                                self.fo[i],
                                self.fe,
                                math.pow(self.fo[i]-self.fe,2),self.fe,
                                self.cuadrados[i])
        str = '{0:-26d} |{1:4d} | {2:-16.2f}'
        print str.format(self.sum_fo, int(self.m)*self.fe, self.sum_cuadrados)


if __name__ == "__main__":
    import sys, os
    directorio =  os.path.join(os.path.dirname(__file__),'..')
    # Agrego el directorio superior a PYTHON_PATH,
    # para que pueda encontrar el modulo util
    sys.path.append(directorio)

    from util.archivo import Archivo
    f = Archivo('/home/ronny/archivos/libro/100numeros.txt')
    valores = f.get_floats()

    print ">>",valores
    test = ChiCuadrado(valores)
    test.start()
    print test.rango_menor
    print ">>...",test.rango_mayor
    print test.fo
    print test.reporte()
