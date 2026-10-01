# Sockets TCP e UDP em Python

Trabalho de Redes de Computadores com duas aplicações cliente-servidor usando a biblioteca `socket`.

**Pedro Henrinque Paschoalim Rossi**                                                               
**Cibersegurança | UFU**

## Arquivos

- `Servidor_TCP.py` / `Cliente_TCP.py`: o cliente envia um número inteiro e o servidor diz se ele é par ou ímpar e se é primo.
- `Servidor_UDP.py` / `Cliente_UDP.py`: o cliente envia uma frase e o servidor responde quantos caracteres ela tem (sem contar espaços).

## Como executar

1. Nos arquivos de cliente, altere `Nome_Servidor` para o IP do servidor (ou `127.0.0.1` para testar na mesma máquina). A porta usada é a `1221`.
2. Inicie o servidor e depois o cliente, em terminais separados:

```bash
# TCP
python Servidor_TCP.py
python Cliente_TCP.py

# UDP
python Servidor_UDP.py
python Cliente_UDP.py
```

Requer apenas Python 3, sem bibliotecas externas.
