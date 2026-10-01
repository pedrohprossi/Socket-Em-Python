from socket import *

Porta_Servidor = 1221
Socket_Servidor = socket(AF_INET, SOCK_DGRAM)
Socket_Servidor.bind(('', Porta_Servidor))

print('Servidor Aguardando Mensagem . . .')

while True:
    Mensagem, Endereco_Cliente = Socket_Servidor.recvfrom(2048)

    Mensagem_Limpa = Mensagem.decode().replace(' ', '')
    Mensagem_Resposta = f'O número de caracteres nessa frase é {len(Mensagem_Limpa)}.'

    Socket_Servidor.sendto(Mensagem_Resposta.encode(), Endereco_Cliente)

    print(f'''
Cliente: {Mensagem.decode()}
Servidor: {Mensagem_Resposta}
''')
    