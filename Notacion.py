from Pila import Pila

def infija_a_sufija(expresionInfija):

    precedencia = {}
    precedencia["*"] = 3
    precedencia["/"] = 3
    precedencia["+"] = 2
    precedencia["-"] = 2
    precedencia["("] = 1
    precedencia["="] = 0

    pilaOperadores = Pila()
    listaSufija = []
    listaSimbolos = expresionInfija.split()

    for simbolo in listaSimbolos:
        if simbolo in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or simbolo.isdigit():
            listaSufija.append(simbolo)
        elif simbolo == '(':
            pilaOperadores.apilar(simbolo)
        elif simbolo == ')':
            simboloTope = pilaOperadores.desapilar()
            while simboloTope != '(':
                listaSufija.append(simboloTope)
                simboloTope = pilaOperadores.desapilar()
        else:
            while (not pilaOperadores.es_vacia()) and \
               (precedencia[pilaOperadores.inspeccionar()] >= \
                precedencia[simbolo]):
                  listaSufija.append(pilaOperadores.desapilar())
            pilaOperadores.apilar(simbolo)

    while not pilaOperadores.es_vacia():
        listaSufija.append(pilaOperadores.desapilar())
    return " ".join(listaSufija)

#print(infija_a_sufija("A * B + C * D"))
#print(infija_a_sufija("( A + B ) * C - ( D - E ) * ( F + G )"))
#print(infija_a_sufija("( 1 + 4 * 6 * ( 4 + 3 ) ) * 4 + ( 4 + 1 ) * 2"))
