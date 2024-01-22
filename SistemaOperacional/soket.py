import socket

#aplicação para comunicação entre computadores
resp = "S"
while(resp=="S"):
    url=input("Digite uma url: ")
    ip=socket.gethostbyname(url)
    print("O IP do endereço é ", ip)
    resp=input("Digite <s> para continuar: "). upper()


