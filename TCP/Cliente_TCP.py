from socket import *
from time import sleep

Nome_Servidor = 'localhost' 
Porta_Servidor = 1221
Socket_Cliente = socket(AF_INET, SOCK_STREAM)
Socket_Cliente.connect((Nome_Servidor,Porta_Servidor))



Mensagem = input('\nDigite um número inteiro: ')


Socket_Cliente.send(Mensagem.encode())
Mensagem_Resposta = Socket_Cliente.recv(2048)

print(f'{Mensagem_Resposta.decode()}\n')

print('Finalizando . . .\n')
sleep(1)



Socket_Cliente.close()

