binario = input("Dame un valor en binario: ")
decimal = 0
longitud = len(binario)
contador = 0
binario_rev = binario[::-1]

while contador < longitud:
    if binario_rev [contador] == 1 :
        decimal = decimal + 2**contador
    contador = contador + 1

print(decimal)