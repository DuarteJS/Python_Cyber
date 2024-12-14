from socket import*
#             localhost
endereco = "127.0.0.1"
porta = 43210

obj_socket = socket(AF_INET, SOCK_STREAM)
obj_socket.bind((endereco, porta))
obj_socket.listen(2)
print("Aguardando Cliente...")

while True:
    conexao, cliente = obj_socket.accept()
    print9("Conectado com; ", cliente )

