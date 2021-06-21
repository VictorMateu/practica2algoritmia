'''
Backtracking iterativo
'''
import sys
import math
class Punto:
    '''
    Clase para almacenar los puntos sobre la tierra
    '''
    def __init__(self, n_points, height, alfa, beta):
        self.puntos = []
        self.costes = 0
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
def ac_iterativo(puntos):
    '''
    Función que realiza el backtracking
    '''
    stack = []
    array_pos = posiciones_iniciales(puntos)
    stack.append(puntos.puntos[0])
    final = False
    coste = []
    coste.append(puntos.alfa*(puntos.height - puntos.puntos[0][1]))
    while not final:
        pos_actual = calcular_posicion(puntos, stack)
        for num in range(pos_actual, puntos.n_points):
            if num == pos_actual:
                array_pos[num] += 1
            else:
                array_pos[num] = num+1
        for num in range(array_pos[pos_actual], puntos.n_points):
            pos_siguiente = calcular_posicion(puntos, stack)
            coste_actual = coste_columna(pos_siguiente, num, puntos)
            coste.append(coste_actual)
            stack.append(puntos.puntos[num])
        coste_actual = 0
        for num in coste:
            if num < 0:
                coste_actual = -1
            elif coste_actual >= 0:
                coste_actual += num
        if puntos.costes == 0:
            puntos.costes = coste_actual
        elif puntos.costes < 0 < coste_actual:
            puntos.costes = coste_actual
        elif puntos.costes > coste_actual > 0:
            puntos.costes = coste_actual
        stack.pop()
        stack.pop()
        coste.pop()
        coste.pop()
        if not stack:
            final = True
    return puntos.costes
def posiciones_iniciales(puntos):
    '''
    Para la posición inicial
    '''
    array_pos = []
    i = 1
    for num in puntos.puntos:
        if num == puntos.puntos[0]:
            array_pos.append(0)
        else:
            array_pos.append(i)
        i+=1
    return array_pos
def calcular_posicion(puntos, stack):
    '''
    Cálculo de la posición
    '''
    k = 0
    for punto in puntos.puntos:
        if punto == stack[-1]:
            return k
        k += 1
    #nunca va a llegar a este return, pero es necesario ponerlo por consistencia del código
    return None
def coste_columna(i,k, puntos):
    '''
    Cálculo de la columna y plataforma
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
    return puntos.beta*(diametro**2) + puntos.alfa*(puntos.height - puntos.puntos[k][1])
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
            for _ in range (0, n_points):
                linea = fichero.readline()
                punto_x, puntos_y = linea.split()
                punto_x = int(punto_x)
                punto_y = int(puntos_y)
                puntos.add_punto(punto_x, punto_y)
            coste_acueducto = ac_iterativo(puntos)
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
        for _ in range (0,n_points):
            linea = sys.stdin.readline()
            punto_x, punto_y = linea.split()
            punto_x = int(punto_x)
            punto_y = int(punto_y)
            puntos.add_punto(punto_x, punto_y)
        coste_acueducto = ac_iterativo(puntos)
        if coste_acueducto < 0:
            print("impossible")
        else:
            print(coste_acueducto)
if __name__ == "__main__":
    main()
