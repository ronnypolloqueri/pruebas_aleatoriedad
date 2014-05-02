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
        self.rango_mayor[i] = 1.0 # el ultimo valor debe ser 1.0
        self.iniciar_conteo()

    def iniciar_conteo(self):
        for i in range(self.fe):
            if i != (self.fe - 1):
                self.fo.append( self.contar( self.rango_menor[i], self.rango_mayor[i], ">" ) )
            else:
                self.fo.append( self.contar( self.rango_menor[i], self.rango_mayor[i], "]" ) )


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
        for i in range(self.fe):
            if i != (self.fe - 1 ) :
                str = '{0:2d} | [ {1:1.2f} : {2:1.2f} > | {3:3d} | {4:3d} |'
            else :
                str = '{0:2d} | [ {1:1.2f} : {2:1.2f} ] | {3:3d} | {4:3d} |'
            print str.format(i+1,
                                                                self.rango_menor[i],
                                                                self.rango_mayor[i],
                                                                self.fo[i],
                                                                self.fe)




if __name__ == "__main__":
    f = open('/home/ronny/archivos/prueba2.txt','r')
    valores = list({})
    for linea in f:
        valores.append(float(linea))
    f.close()
    print ">>",valores
    test = ChiCuadrado(valores)
    test.start()
    print test.rango_menor
    print ">>...",test.rango_mayor
    print test.fo
    print test.reporte()
