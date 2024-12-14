# FTP -  file transfer protocol

from ftplib import*

ftp = FTP("ftp.ibge.gov.br")
# ftp = FTP("ftp.ibiblio.org")


print(ftp.getwelcome())


usuario = input("Informe um usuario: ")
senha = input("Infome uma senha: ")

ftp.login (usuario, senha)

print("Pasta atual: ", ftp.pwd())

print(ftp.retrlines('LIST'))

ftp.quit()