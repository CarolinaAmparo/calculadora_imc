# Carolina Amparo
# Programa que pide al usuario su nombre, apellido paterno, apellido materno, edad, peso y estatura 
# desplegarlos en pantalla junto con su Índice de Masa Corporal (IMC).


#Validacion de Ingreso de datos tipo string con metodo isalpha
# para comprobar que el usuario ingreso solo letras.
while True:
    nombre = input("INGRESA TU NOMBRE: ")
    tipo_n = nombre.isalpha()
    if tipo_n == False:
        print("LA ENTRADA DE DATOS ES INVALIDA ESCRIBA NOMBRE")
        continue
    break
while True:
    apellido_p = input("INGRESE SU APELLIDO PATERNO: ")
    tipo_a = apellido_p.isalpha()
    if tipo_a == False:
        print("LA ENTRADA DE DATOS ES INVALIDA ESCRIBA APELLIDO")
        continue
    break
while True:
    apellido_m = input("INGRESE SU APELLIDO MATERNO: ")
    tipo_b = apellido_m.isalpha()
    if tipo_b == False:
        print("LA ENTRADA DE DATOS ES INVALIDA ESCRIBA APELLIDO")
        continue
    break
#Validacion de ingreso de datos tipo int e invalidando datos tipo str, float o numeros negativos
while True:
    try:
        edad = int(input("INGRESA TU EDAD: "))
    except ValueError:
        print("DEBES INGRESAR NUMERO ENTERO")
        continue

    if edad < 0:
        print("DEBES INGRESAR UN NUMERO POSITIVO.")
        continue
    else:
        break
#Validacion de datos tipo float e invalidando otros caracteres y numeros negativos
while True:
    try:
        peso = float(input("INGRESA TU PESO EN KILOGRAMOS: "))
    except ValueError:
        print("DEBES INGRESAR NUMEROS")
        continue

    if peso < 0:
        print("DEBES INGRESAR UN NUMEROS POSITIVOS.")
        continue
    else:
        break
while True:
    try:
        est = float(input("INGRESA TU ESTATURA: "))
    except ValueError:
        print("DEBES INGRESAR NUMEROS")
        continue

    if est < 0:
        print("DEBES INGRESAR UN NUMEROS POSITIVOS.")
        continue
    else:
        break

# Formula para calcular IMC
IMC= peso / est ** 2
#{str(IMC)}
#IMC = IMC
#Impresion de datos en pantalla añadiendo el IMC
print(f" \n \n \t \t \t HOLA {nombre} {apellido_p} {apellido_m} TU IMC ACTUALMENTE ES: {round(IMC, 2)}  ")

#Hacemos las distintas validaciones
if IMC >= 0 and IMC <= 15.99 :
    print (" \t \t \t RANGO CONSIDERADO COMO DELGADEZ SEVERA \n")
elif IMC >= 16.00 and IMC <= 16.99 :
    print (" \t \t \t RANGO CONSIDERADO COMO DELGADEZ MODERADA \n")
elif IMC >= 17.00 and IMC <= 18.49:
    print (" \t \t \t RANGO CONSIDERADO COMO DELGADEZ LEVE \n")
elif IMC >= 18.50 and IMC <= 24.99 :
    print (" \t \t \t RANGO CONSIDERADO COMO NORMAL \n")
elif IMC >= 25.00 and IMC <= 29.99:
    print (" \t \t \t RANGO CONSIDERADO COMO SOBREPESO \n")
elif IMC >= 30.00 and IMC <= 34.99:
    print (" \t \t \t RANGO CONSIDERADO COMO OBESIDAD LEVE \n")
elif IMC >= 35.00 and IMC <= 39.00:
    print (" \t \t \t RANGO CONSIDERADO COMO OBESIDAD MEDIA \n")
elif IMC >= 40.00:
    print (" \t \t \t RANGO CONSIDERADO COMO OBESIDAD MORBIDA \n")








