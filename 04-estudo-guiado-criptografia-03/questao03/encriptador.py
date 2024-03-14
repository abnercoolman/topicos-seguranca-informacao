from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import timeit

# Geração da chave de criptografia
chave = Fernet.generate_key()

# Algoritmos e tamanhos de chave
algoritmos_chaves = {
    "AES-128": 16,
    "AES-256": 32,
    "ChaCha20": 32
}

# Geração de objetos Fernet para cada algoritmo
cipher_suites = {}
for nome_algoritmo, tamanho_chave in algoritmos_chaves.items():
    # Seleciona os bytes necessários da chave baseado no tamanho do algoritmo
    chave_algoritmo = chave[:tamanho_chave]

    # Cria o objeto Cipher
    algoritmo = algorithms.AES(chave_algoritmo)
    modo = modes.CBC(chave[:16])  # Mantém o vetor de inicialização (IV) fixo
    cipher = Cipher(algoritmo, modo)

    # Cria o objeto Fernet usando a chave original
    cipher_suites[nome_algoritmo] = Fernet(chave)

# Salva a chave em um arquivo
with open('chave_secreta.txt', 'wb') as arquivo_chave:
    arquivo_chave.write(chave)

print('Chave gerada e salva em "chave_secreta.txt".')

# Criptografia e descriptografia com diferentes tamanhos de chave
for nome_algoritmo, cipher_suite in cipher_suites.items():
    # Criptografia
    with open('arquivo.txt', 'rb') as arquivo:
        texto = arquivo.read()
        texto_criptografado = cipher_suite.encrypt(texto)

    # Salva o texto cifrado em um novo arquivo
    with open(f'arquivo_criptografado_{nome_algoritmo}.txt', 'wb') as arquivo_criptografado:
        arquivo_criptografado.write(texto_criptografado)

    # Descriptografia
    with open(f'arquivo_criptografado_{nome_algoritmo}.txt', 'rb') as arquivo_criptografado:
        texto_criptografado = arquivo_criptografado.read()
        texto_descriptografado = cipher_suite.decrypt(texto_criptografado)

    # Salva o texto descriptografado em um novo arquivo
    with open(f'arquivo_descriptografado_{nome_algoritmo}.txt', 'wb') as arquivo_descriptografado:
        arquivo_descriptografado.write(texto_descriptografado)

    # Cálculo do tempo de excução do código
    tempo = timeit.timeit(number=1)

    print(
        f'Arquivo "arquivo.txt" criptografado e descriptografado com o algoritmo {nome_algoritmo}.')
    print(f"Tempo de execução: {tempo:.12f} s.\n")
