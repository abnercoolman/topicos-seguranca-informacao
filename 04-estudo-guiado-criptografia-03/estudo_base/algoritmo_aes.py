from cryptography.fernet import Fernet

# Geração da chave de criptografia
chave = Fernet.generate_key()
cipher_suite = Fernet(chave)

# Leitura e encriptografia do conteúdo do arquivo
with open('arquivo.txt', 'rb') as arquivo:
    texto = arquivo.read()
    texto_cifrado = cipher_suite.encrypt(texto)

# Salva o texto cifrado em um novo arquivo
with open('arquivo_cifrado.txt', 'wb') as arquivo_cifrado:
    arquivo_cifrado.write(texto_cifrado)

# Leitura do arquivo criptografado e descriptografia do conteúdo
with open('arquivo_cifrado.txt', 'rb') as arquivo_cifrado:
    texto_cifrado = arquivo_cifrado.read()
    texto_decifrado = cipher_suite.decrypt(texto_cifrado)

# Salva o texto decifrado em um novo arquivo
with open('arquivo_decifrado.txt', 'wb') as arquivo_decifrado:
    arquivo_decifrado.write(texto_decifrado)


def comparar_arquivos(arquivo_original, arquivo_decifrado):

    with open(arquivo_original, 'rb') as original, open(arquivo_decifrado, 'rb') as descrypt:
        # Utilizamos o 'while' pois há uma comparação dos dois arquivos byte a byte.
        while True:
            texto_original = original.read(1)
            texto_decifrado = descrypt.read(1)

            if texto_original != texto_decifrado:
                return False

            if not texto_original or not texto_decifrado:
                break

    return True


resultado = comparar_arquivos("arquivo.txt", "arquivo_decifrado.txt")

if resultado:
    print("Os arquivos são idênticos.")
else:
    print("Os arquivos são diferentes.")