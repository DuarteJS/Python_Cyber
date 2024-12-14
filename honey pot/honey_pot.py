from socket import *
import logging

logging.basicConfig(filename="honeypot.log", level=logging.INFO, format = '%(asctime)s - %(message)s')

def iniciar_honeypot(endereco, porta):
    meu_socket = socket(AF_INET, SOCK_STREAM)

    meu_socket.bind((endereco, porta))

    meu_socket.listen(5)
    print("Honeypot rodando no endereco e porta: ", endereco , porta)

    while True:

        socket_cliente, endereco_cliente = meu_socket.accept()

        print("Conexao vinda de: ", endereco_cliente)

        logging.info(f"Conexao vinda de {endereco_cliente} " )

        socket_cliente.close()

iniciar_honeypot("127.0.0.1", 8080)
