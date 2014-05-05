class CorridasArribaAbajo(object):
    """docstring for CorridasArribaAbajo"""
    def __init__(self, numeros):
        self.numeros = numeros
        self.n = self.numeros.__len__()
        self.unos_y_ceros = list({})
        self.numero_de_corridas = -1
        self.start()

    def start(self):
        for i in range(1,self.n): # del 1 al n-1( ya que comienza en cero
            # Si el numero es menor o igual que el anterior se pone cero
            if self.numeros[i] <= self.numeros[i-1]:
                self.unos_y_ceros.append(0)
            else: # Si no se pone 1
                self.unos_y_ceros.append(1)

            if i == 1: # Si ES el primer caso
                self.numero_de_corridas = 1
            else: # Si NO es el primer caso y el anterior es diferente al actual => +1 corrida
                if self.unos_y_ceros[i-1] != self.unos_y_ceros[i-2]:
                    self.numero_de_corridas += 1

    def __str__(self):
        return "Numeros ingresados: %s\nSecuencia: %s\nNumero de corridas: %s"%(self.numeros, self.unos_y_ceros, self.numero_de_corridas)


if __name__ == '__main__':
    import os, sys
    dir = os.path.join(os.path.dirname(__file__),'..')
    sys.path.append(dir)
    from util.archivo import Archivo
    numeros = Archivo('/home/ronny/archivos/libro/prueba_independencia.txt').get_floats()
    cab = CorridasArribaAbajo(numeros)
    print cab
