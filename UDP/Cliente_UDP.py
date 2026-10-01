from socket import *
from time import sleep

Nome_Servidor = '10.0.99.150' 
Porta_Servidor = 1221
Socket_Cliente = socket(AF_INET, SOCK_DGRAM)
Socket_Cliente.settimeout(5)

while True:
    Mensagem = input('Escreva uma frase que deseja contar os caracteres: ')

    Socket_Cliente.sendto(Mensagem.encode(), (Nome_Servidor, Porta_Servidor))
    
    try: 
        Mensagem_Resposta, Endereco_Servidor = Socket_Cliente.recvfrom(2048)
        print(Mensagem_Resposta.decode())
    except timeout:
        print('Pacote perdido ou servidor fora do ar.')


    continuar = input('\nDeseja enviar outra mensagem? [S/N] ').upper().strip()
    while continuar not in ('S','N'):
        continuar = input('Deseja enviar outra mensagem? [S/N] ').upper().strip()

    if continuar == 'S':
        print('Reiniciando . . .\n')
        sleep(1)
    else:
        print('Finalizando . . .\n')
        sleep(1)
        break

Socket_Cliente.close()

    
