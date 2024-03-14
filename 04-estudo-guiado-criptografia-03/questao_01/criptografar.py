from cryptography.fernet import Fernet

# Leitura da chave secreta
with open('chave_secreta.txt', 'rb') as arquivo_chave:
    chave = arquivo_chave.read()

# Cria o objeto Fernet com a chave
cipher_suite = Fernet(chave)

# Leitura e encriptografia do conteúdo do arquivo
with open('arquivo.txt', 'rb') as arquivo:
    texto = arquivo.read()
    texto_cifrado = cipher_suite.encrypt(texto)

# Salva o texto cifrado em um novo arquivo
with open('arquivo_criptografado.txt', 'wb') as arquivo_criptografado:
    arquivo_criptografado.write(texto_cifrado)

print('Arquivo "arquivo.txt" criptografado e salvo como "arquivo_criptografado.txt".')