from Pila import Pila

def evaluacionNotacionSufija(expresionSufija):
    pilaOperandos = Pila()
    listaSimbolos = expresionSufija.split()

    for simbolo in listaSimbolos:
        if simbolo in "*/+-=":
            operando2 = pilaOperandos.desapilar()
            operando1 = pilaOperandos.desapilar()
            # resultado = hacerAritmetica(simbolo,operando1,operando2)
            

            #print(operando1,simbolo,operando2)
            pilaOperandos.apilar("{} {} {}".format(simbolo,operando1,operando2))
        else:
            pilaOperandos.apilar((simbolo))
    return pilaOperandos.desapilar()

def hacerAritmetica(operador, operandoIzquierda, operandoDerecha):
    if operador == "*":
        return operandoIzquierda * operandoDerecha
    elif operador == "/":
        return operandoIzquierda / operandoDerecha
    elif operador == "+":
        return operandoIzquierda + operandoDerecha
    else: 
        return operandoIzquierda - operandoDerecha

#print(evaluacionNotacionSufija('12 2 * 3 7 * + 10 +'))

#print(evaluacionNotacionSufija('2 3 4 * + '))

def Triplos(expresionSufija):
    cont = 0
    pilaOperandos = Pila()
    listaSimbolos = expresionSufija.split()

    for simbolo in listaSimbolos:
        if simbolo in "*/+-=":
            operando2 = pilaOperandos.desapilar()
            operando1 = pilaOperandos.desapilar()
            # resultado = hacerAritmetica(simbolo,operando1,operando2)

            print ("{:<8} {:<8} {:<15} {:<10}".format('({})'.format(cont), simbolo,operando1,operando2))
            
            #pilaOperandos.apilar("{} {} {}".format(simbolo,operando1,operando2))
            pilaOperandos.apilar('({})'.format(cont))
            cont += 1

        else:
            pilaOperandos.apilar((simbolo))
    return pilaOperandos.desapilar()

def Cuadruplos(expresionSufija):
    cont = 0
    pilaOperandos = Pila()
    listaSimbolos = expresionSufija.split()

    for simbolo in listaSimbolos:
        if simbolo in "*/+-":
            operando2 = pilaOperandos.desapilar()
            operando1 = pilaOperandos.desapilar()
            # resultado = hacerAritmetica(simbolo,operando1,operando2)

            print ("{:<8} {:<15} {:<10} {:<8}".format(simbolo,operando1,operando2,'T{}'.format(cont)))
            
            #pilaOperandos.apilar("{} {} {}".format(simbolo,operando1,operando2))
            pilaOperandos.apilar('T{}'.format(cont))
            cont += 1
        elif simbolo == "=": 
            print ("{:<8} {:<15} {:<10} {:<8}".format(simbolo,pilaOperandos.desapilar(),'',listaSimbolos[0]))  
        else:
            pilaOperandos.apilar((simbolo))
    return pilaOperandos.desapilar()
