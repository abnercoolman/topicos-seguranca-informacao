import socket
from cryptography.fernet import Fernet


def encrypt_file(key):
    """
    Criptografa o conteúdo de 'arquivo.txt' usando a chave fornecida.
    - Argumentos: A chave de criptografia.
    - Retorna: O conteúdo criptografado do arquivo.
    """

    with open('arquivo.txt', 'rb') as file:
        texto = file.read()
    cipher_suite = Fernet(key)
    texto_encriptado = cipher_suite.encrypt(texto)

    return texto_encriptado


def servidor(nome_servidor):
    """
    Cria um socket de servidor, escuta conexões, criptografa um arquivo,
    e envia o conteúdo criptografado para o cliente conectado.
    - Argumentos: O nome do servidor.
    """

    SERVER_ADDRESS = ('', 5000)  # Vincula a todas as interfaces na porta 5000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind(SERVER_ADDRESS)
        server_socket.listen(1)

        print(f"Olá, {nome_servidor}. Servidor aguardando conexão...")

        connection, client_address = server_socket.accept()
        with connection:
            print(f"Conectado a {client_address}")

            # Recebe o nome do cliente (opcional)
            # nome_cliente = connection.recv(1024).decode()
            # connection.sendall(nome_servidor.encode())

            # Gera uma nova chave de criptografia
            key = Fernet.generate_key()

            # Envia a chave ao cliente (considere métodos seguros de troca de chaves)
            connection.sendall(key)

            # Criptografa o arquivo e envia o conteúdo criptografado
            texto_encriptado = encrypt_file(key)
            connection.sendall(texto_encriptado)

            print("Arquivo enviado com sucesso.")


if __name__ == '__main__':
    nome_servidor = input("Digite o nome do servidor: ")
    servidor(nome_servidor)
