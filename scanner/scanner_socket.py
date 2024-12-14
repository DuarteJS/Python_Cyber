from socket import *
#  * = tudo

import time

# Pegar o tempo inicial
tempo_inicial = time.time()

alvo = input("Informe o IP para ser escaneado: ")

ip_alvo = gethostbyname(alvo)

print("Começando scan: ", ip_alvo)

# Threading - executar varias taferas ao mesmo tempo
for i in range (50, 500):
    s = socket(AF_INET, SOCK_STREAM)

    # tento me conectar na porta
    conexao = s.connect_ex((ip_alvo, i))
    # i = portas

    if conexao == 0:
        print("Porta: ", i, "aberta")

    s.close()
   
   
print("Tempo que levou: ", time.time() - tempo_inicial )

   