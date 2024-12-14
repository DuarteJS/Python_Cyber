from socket import*
#             localhost
endereco = "127.0.0.1"

porta = 43210

while True:
    # IPV4 e o IPV6
    # AF_INET - IPv4

    # TCP ou UDP
    # TCP - mais segura
    # UDP - Menos segurp e mais rapido
    obj_socket = socket(AF_INET, SOCK_STREAM)
    obj_socket.connect((endereco, porta))
    msg = bytes(input("Mensagem: "), 'utf-8')
    obj_socket.send(msg)