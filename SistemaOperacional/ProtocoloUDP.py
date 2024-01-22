from socket import *

servidor="127.0.0.1"
porta=43210

obj_socket = socket(AF_INET, SOCK_DGRAM) #criando o objeto socket com nome do servidor e definindo o protocolo udp (sock_degram)
obj_socket.bind((servidor,porta)) #disponibilizando o endereço com a porta
print("Servidor pronto....")

while True:
    dados, origem = obj_socket.recvfrom(65535) #quantidade de maxima de porta, retornando quem é o cliente (origem) e quais são os dados
    print("Origem..........: ", origem)
    print("Dados recebidos.: ", dados.decode()) #decodificando as informações recebidas
    resposta=input("Digite a resposta: ") # criando a resposta pelo servidor
    obj_socket.sendto(resposta.encode(), origem) #enviando a resposta do servidor

obj_socket.close()