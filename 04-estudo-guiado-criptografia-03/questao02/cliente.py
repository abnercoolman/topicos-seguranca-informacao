import socket
from cryptography.fernet import Fernet


def receive_file(connection, key):
    """
    Recebe o conteúdo criptografado de um arquivo do servidor, descriptografa-o,
    e salva em um novo arquivo.
    - Argumentos:
        * conexão: O socket conectado.
        * chave: A chave de criptografia.
    """

    with open('arquivo_recebido.txt', 'wb') as file_received:
        # Recebe o conteúdo criptografado
        texto_encriptado = b''
        while True:
            data = connection.recv(1024)
            if not data:
                break
            texto_encriptado += data

        # Salva o conteúdo criptografado em "arquivo_recebido.txt"
        file_received.write(texto_encriptado)

    with open('arquivo_descriptografado.txt', 'wb') as file_decrypted:
        # Descriptografa o conteúdo
        cipher_suite = Fernet(key)
        texto_descriptografado = cipher_suite.decrypt(
            texto_encriptado.decode())

        # Salva o conteúdo descriptografado em "arquivo_descriptografado.txt"
        file_decrypted.write(texto_descriptografado)

    print("Arquivo recebido e decifrado com sucesso!")


def client(nome_cliente, endereco_servidor):
    """
    Se conecta ao servidor, recebe a chave de criptografia e descriptografa
    o arquivo recebido.
    - Argumentos:
        * nome_cliente: O nome do cliente.
        * endereco_servidor: O endereço do servidor (host, porta).
    """

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect(endereco_servidor)

        # Envia o nome do cliente (opcional)
        # cliente_socket.sendall(nome_cliente.encode())

        # Recebe a chave do servidor
        key = client_socket.recv(1024)

        receive_file(client_socket, key)


if __name__ == '__main__':
    nome_cliente = input("Digite o nome do cliente: ")
    endereco_servidor = ('localhost', 5000)

    client(nome_cliente, endereco_servidor)
