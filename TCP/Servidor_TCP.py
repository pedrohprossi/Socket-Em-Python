from socket import *

def par_impar(num):
    if num % 2 == 0:
        return 'par'
    else:
        return 'ímpar'
    
def primo(num):
    if num < 2:
            return 'não é primo'
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return 'não é primo'
    else: 
        return 'é primo'


Porta_Servidor = 1221
Socket_Servidor = socket(AF_INET, SOCK_STREAM)
Socket_Servidor.bind(('', Porta_Servidor))

Socket_Servidor.listen(1)

print('Servidor conectado . . . ')
print('Histórico')
print('')
while True:
    Socket_Conexao , Endereco = Socket_Servidor.accept()

    Mensagem = Socket_Conexao.recv(2048).decode().strip()
    try:
        num = int(Mensagem)
        Mensagem_Resposta = f'O número {num} é {par_impar(num)} e {primo(num)}.'
    except ValueError:
        Mensagem_Resposta = 'Mande um número inteiro'

    print(f'''Cliente: {Mensagem}
Servidor: {Mensagem_Resposta}
''')

    Socket_Conexao.send(Mensagem_Resposta.encode())
    Socket_Conexao.close()