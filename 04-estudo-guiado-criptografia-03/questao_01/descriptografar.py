from cryptography.fernet import Fernet

# Leitura da chave secreta
with open('chave_secreta.txt', 'rb') as arquivo_chave:
    chave = arquivo_chave.read()

# Cria o objeto Fernet com a chave
cipher_suite = Fernet(chave)

# Leitura do conteúdo do arquivo criptografado
with open('arquivo_criptografado.txt', 'rb') as arquivo_criptografado:
    texto_criptografado = arquivo_criptografado.read()

# Descriptografia do texto
texto_descriptografado = cipher_suite.decrypt(texto_criptografado)

# Salva o texto descriptografado em um novo arquivo
with open('arquivo_descriptografado.txt', 'wb') as arquivo_descriptografado:
    arquivo_descriptografado.write(texto_descriptografado)

print('Arquivo "arquivo_criptografado.txt" descriptografado e salvo como "arquivo_descriptografado.txt".')