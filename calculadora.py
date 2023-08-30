print("Por favor introduzca el numero a la operación a realizar:")

print("1. Binario a decimal")
print("2. Decimal a binario")
print("3. Suma")
print("4. Resta")
print("5. Multiplicacion")
print("6. División")

user = int(input())

if user == 1 :
    uno_binario = input("Dame un valor en binario: ")
    uno_decimal = 0
    uno_longitud = len(uno_binario)
    uno_contador = 0
    uno_binario_rev = uno_binario[::-1]

    while uno_contador < uno_longitud:
        if uno_binario_rev [uno_contador] == 1 :
            uno_decimal = uno_decimal + 2**uno_contador
        uno_contador = uno_contador + 1

    print(uno_decimal)

elif user == 2 :
    dos_decimal = input("Inserta los decimales a convertir a binario: ")
    dos_binario = ""
    dos_cociente = int(dos_decimal)

    while dos_cociente != 1 :
        dos_residuo = dos_cociente % 2
        dos_cociente = dos_cociente // 2
        dos_binario = dos_binario + str(dos_residuo)

    dos_binario = dos_binario + str(dos_residuo)
    dos_res = dos_binario [::-1]
    print(dos_res)

elif user == 3 :
    suma_n1 = int(input("Ingrese el primer numero a sumar: "))
    suma_n2 = int(input("Ingrese el segundo numero a sumar: "))
    suma_tot = suma_n1 + suma_n2
    print(suma_tot)

elif user == 4 :
    resta_n1 = int(input("Ingrese el primer numero a restar: "))
    resta_n2 = int(input("Ingrese el segundo numero a restar"))
    resta_tot = resta_n1 - resta_n2
    print(resta_tot)

elif user == 5 :
    mult_n1 = int(input("Ingrese el primer numero a multiplicar: "))
    mult_n2 = int(input("Ingrese el segundo numero a multiplicar: "))
    mult_tot = mult_n1 * mult_n2
    print(mult_tot)

elif user == 6 :
    div_n1 = int(input("Ingrese el primer numero a dividir: "))
    div_n2 = int(input("Ingrese el segundo numero a dividir: "))
    div_tot = div_n1 / div_n2
    print(div_tot)

elif user >= 7 :
    print("El numero ingresado no es valido.")

print("Cerrando programa.")