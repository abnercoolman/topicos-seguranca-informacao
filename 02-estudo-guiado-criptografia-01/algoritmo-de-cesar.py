# Variável que armazena o texto a ser criptografado
texto = input('Digite o texto que deseja criptografar: ')

# Variável que armazena a distância para criptografar o texto
distancia = int(input('Digite a distância que deseja usar: '))

# Variável que armazenará o texto criptografado
cripto = ''

# Algoritmo de César
for letra in texto:
    numero = ord(letra)
    numero = numero + distancia
    letra = chr(numero)
    cripto = cripto + letra

print('O texto criptografado é: ' + cripto)