#texto_variado = "palabra 123 +-"
#print(type(texto_variado))

#Podemos utilizar comillas tripes para que el texto se muestre como la cadena que hemos escrito
# print(""""
# funcionamiento de \
# programa: (opciones)
# -1 Para acceder a oopciones
# -2 Para salir
# """)

# Subscripting  e indexado

# texto = "Python"

# print(texto[0])
# print(texto[5])
# print(texto[-1])
# print(texto[-6])

# print(texto[6]) #no podemos acceder a una posicion que no existe

# letra = texto[0]
# print(letra)

# # texto[0] = "p" # error no podemos mpodificar una cadena
# letra = "p"
# print(letra)

# texto_compuesto = letra + texto[1] #concatenacion
# print(texto_compuesto)


##########################################################################

#Sliciong o Substringing
# texto = "Python"

# print(texto[0:3])
# print(texto[0:-3])
# print(texto[0:-2])
# print(texto[2:])
# print(texto[:3])

# print(texto[-3::-1])
# print(texto[::-1])
#print(texto[1:50])
# print(texto[2:2])

############################################################################

#Cadenas y Formatos

# texto ="Hola Mundo! Buenastardes"
# print(texto.lower())  #Homologar a minusculas
# print(texto.upper()) #Homologar a mayusculas
# print(texto.capitalize()) #Primera letra mayuscula
# print(texto.title()) # Inicial de cada palabra con mayuscula
# print(texto.swapcase()) #Intercambia minusculas por mayusculas
# texto =texto.upper()
# print(texto)

print("{} + {} = {}".format(2,3, 2 + 3))
print("{} + {} = {}".format("hola", "mundo", "Hola mundo"))
print("{:.3f} + {:.4f} = {}".format(2, 3, 2 + 3))
print("{1} + {0} = {2}".format(2, 3, 2+3))
print("{2} + {0} = {1}".format("hola", "mundo", "Hola mundo"))
print("{:d}  = {:b} = {:o}  = {:x}".format(15, 15, 15, 15))



