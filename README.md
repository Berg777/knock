<div align="center">
  
# Script de Port Knocking em Python
<img src="https://cdn.discordapp.com/attachments/888582916651773985/1243045333148242081/image.png?ex=66500bae&is=664eba2e&hm=11acc37c8c55b06a6d96f535e829a25708441442ddda654abb2f3d455ddf2178&">
</div>

Este é um script simples em Python para realizar o procedimento de port knocking em um servidor remoto. O port knocking é uma técnica de segurança usada para aumentar a segurança de um servidor ao ocultar os serviços disponíveis até que uma sequência específica de conexões seja feita.

<div align="center">

# Funcionalidades
</div>

- Suporte para TCP e UDP.
- Personalização da sequência de port knocking através de argumentos de linha de comando.
- Implementação básica de port knocking usando sockets em Python.

<div align="center">

# Requisitos
</div>

- Python 3.x

<div align="center">

# Uso
</div>

**Uso padrão:**

O script pode ser executado a partir da linha de comando, especificando o endereço IP do servidor alvo e a sequência de portas e protocolos de knocking desejados. Aqui está um exemplo de uso:


```sh
./knock.py 172.16.1.100 8001 TCP 7002 UDP 9003 TCP
```

Neste exemplo, o script realizará knocking na porta 8001 usando TCP, em seguida, na porta 7002 usando UDP e finalmente na porta 9003 usando TCP.

<br>

**Realizando scan na porta desejada:**

```sh
./knock.py 172.16.1.100 8001 TCP 7002 UDP 9003 TCP --scan 22 TCP
```

Neste exemplo, o script irá:

- Realizar um escaneamento de portas no servidor remoto (172.16.1.100).
- Após o escaneamento, realizar port knocking nas portas 8001 (TCP), 7002 (UDP) e 9003 (TCP).
- Verificar o estado da porta 22 (TCP) para determinar se o procedimento de port knocking foi bem-sucedido.
