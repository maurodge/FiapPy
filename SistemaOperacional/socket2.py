#aplicação para abrir uma conexão
from socket import *

servidor="127.0.0.1" #localhost
porta=43210

obj_socket = socket(AF_INET, SOCK_STREAM) #socket_stream para trabalhar com o TCP
obj_socket.bind((servidor,porta)) #configuração da conexao
obj_socket.listen(2) # quantos clientes podem acessar 

print("Aguardando cliente....")

while True:
    con, cliente = obj_socket.accept() #estabelecendo uma conexão
    print("Conectado com: ", cliente)
    while True:
        msg_recebida = str(con.recv(1024)) #metodo para receber é o recv
        print("Recebemos: ", msg_recebida)
        msg_enviada = b'Olah cliente'
        con.send(msg_enviada)
        break
    con.close()