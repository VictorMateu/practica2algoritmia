'''
Dynamic Programing iterativo
'''
import sys
import math
class Punto:
    '''
    Clase para almacenar los puntos sobre la tierra
    '''
    def __init__(self, n_points, height, alfa, beta):
        self.puntos = []
        self.costes = {}
        self.n_points = n_points
        self.height = height
        self.alfa = alfa
        self.beta = beta
    def add_punto(self, punto_x, punto_y):
        '''
        Añade un punto del terreno
        '''
        self.puntos.append([punto_x, punto_y])
    def add_coste(self, costes):
        '''
        Añade el coste
        '''
        self.costes += costes
def ac_iterativo(puntos, i):
    '''
    Función que realiza dynamic programing
    '''
    while i >= 0:
        costes = {}
        k = i
        while k < puntos.n_points-1:
            coste_actual = calcular_coste(i, k+1 , puntos)
            if coste_actual > 0:
                costes[k] = calcular_coste(i, k+1 , puntos)
            k += 1
            if costes:
                puntos.costes[i] = min(costes.values())
            else:
                puntos.costes[i] = -1
        if k == puntos.n_points-1:
            puntos.costes[k] = puntos.alfa*(puntos.height - puntos.puntos[k][1])
        i -= 1
    return puntos.costes[0]
def calcular_coste(i, k, puntos):
    '''
    Función que calcula el coste
    '''
    coste_actual = coste_columna(i, k, puntos)
    if coste_actual < 0 or puntos.costes[k] < 0:
        return -1
    return coste_actual + puntos.costes[k]
def coste_columna(i,k, puntos):
    '''
    Función que calcula el coste de la columna y plataforma
    '''
    diametro = puntos.puntos[k][0] - puntos.puntos[i][0]
    radio = float(diametro/2)
    altura_izq = puntos.height - puntos.puntos[i][1]
    altura_drc = puntos.height - puntos.puntos[k][1]
    if altura_izq < radio or altura_drc < radio or \
    puntos.puntos[i][1] >= puntos.height or puntos.puntos[k][1] >= puntos.height:
        return -1
    centro_x = puntos.puntos[i][0] + radio
    centro_y = puntos.height - radio
    for punto in range (i+1, k):
        result_y = math.sqrt(radio**2 - (puntos.puntos[punto][0] - centro_x)**2) + centro_y
        if puntos.puntos[punto][1] > result_y:
            return -1
    return puntos.beta*(diametro**2) + puntos.alfa*(puntos.height - puntos.puntos[i][1])
def main():
    '''
    Función principal:
    Obtiene los datos ya sea por linea de comandos o a través de un fichero
    '''
    if len(sys.argv) > 1:
        args = sys.argv[1:]
        with open(args[0], "r") as fichero:
            linea = fichero.readline()
            n_points, height, alfa, beta = linea.split()
            n_points = int(n_points)
            height = int(height)
            alfa = int(alfa)
            beta = int(beta)
            puntos = Punto(n_points,height,alfa,beta)
            for linea in range (0,n_points):
                linea = fichero.readline()
                punto_x, punto_y = linea.split()
                punto_x = int(punto_x)
                punto_y = int(punto_y)
                puntos.add_punto(punto_x, punto_y)
            k = puntos.n_points-1
            coste_acueducto = ac_iterativo(puntos, k)
            if coste_acueducto < 0:
                print("impossible")
            else:
                print(coste_acueducto)
    else:
        linea = sys.stdin.readline()
        n_points, height, alfa, beta = linea.split()
        n_points = int(n_points)
        height = int(height)
        alfa = int(alfa)
        beta = int(beta)
        puntos = Punto(n_points,height,alfa,beta)
        for linea in range (0,n_points):
            linea = sys.stdin.readline()
            punto_x, punto_y = linea.split()
            punto_x = int(punto_x)
            punto_y = int(punto_y)
            puntos.add_punto(punto_x, punto_y)
        k = puntos.n_points-1
        coste_acueducto = ac_iterativo(puntos, k)
        if coste_acueducto < 0:
            print("impossible")
        else:
            print(coste_acueducto)
if __name__ == "__main__":
    main()
