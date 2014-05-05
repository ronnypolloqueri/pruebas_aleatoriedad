import math


def contar(valores):
    return valores.__len__()

def suma(valores):
    sum = 0
    for valor in valores:
        sum += valor
    return sum

def media(valores):
    return float(suma(valores)) / valores.__len__()

def sumatoria_del_cuadrado_de_las_diferencias(valores):
    _media = media(valores)
    sum = 0
    for valor in valores:
        sum += math.pow(valor - _media , 2)
    return sum

def test(valores):
    print "=" * 20
    print "valores: %s " % valores
    print "n: %s " % contar(valores)
    print "suma: %s " % suma(valores)
    print "media: %s " % media(valores)
    print "sumatoria del cuadrado de las diferencias: %s" % sumatoria_del_cuadrado_de_las_diferencias(valores)
if __name__ == "__main__":
    test( range(1,11) ) # del 1 al 10
    test( range(2,5) ) # del 1 al 10
    test( range(7,10) ) # del 1 al 10
