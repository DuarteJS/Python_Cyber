from ftplib import*

ftp = FTP("ftp.ibge.gov.br")
#ftp = FTP("ftp.ibiblio.org")

print(ftp.getwelcome())

print("Pasta atual: ", ftp.pwd())