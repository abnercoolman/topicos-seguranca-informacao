from cryptography.fernet import Fernet

# Geração da chave de criptografia
chave = Fernet.generate_key()

# Salva a chave em um arquivo
with open('chave_secreta.txt', 'wb') as arquivo_chave:
    arquivo_chave.write(chave)

print('Chave gerada e salva em "chave_secreta.txt".')