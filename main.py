from Notacion import infija_a_sufija
from Evaluar import Triplos,Cuadruplos

#expresion = input("Expresión: ")

# expresion = "X = 1 + 4 * 6 * ( 4 + 3 ) "

#expresion = "( A - B ) * C + D / E"

expresion = "24 * ( 150 + 6000 - ( 81 / 20 * 3 ) - 789 ) - 100"

posfija = infija_a_sufija(expresion)

print("---------------------------------------------------------")
print("\n Expresion: ",expresion)
print(" Sufija: ",posfija)
print("")

print("\n Triplos")
print ("{:<8} {:<8} {:<15} {:<10}".format('', 'op','arg1','arg2'))
Triplos(posfija)
print("---------------------------------------------------------")

print("\n Cuadruplos")
print ("{:<8} {:<15} {:<10} {:<8}".format('op','arg1','arg2','Result'))
Cuadruplos(posfija)
print("---------------------------------------------------------")
print("")
