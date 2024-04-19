import sys
import socket
import time
import argparse

# Dicionário de cores
colors = {
    "reset": "\033[0m",
    "bold": "\033[1m",
    "yellow": "\033[1;33m",
    "blue": "\033[1;34m",
    "green": "\033[1;32m",
    "red": "\033[1;31m",
    "purple": "\033[1;35m",
}

def knock_tcp(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((ip, port))
    sock.close()
    return result == 0

def knock_udp(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(1)
    sock.sendto(b'', (ip, port))
    try:
        data, addr = sock.recvfrom(1024)
    except socket.timeout:
        pass
    finally:
        sock.close()

def scan_port(ip, port, protocol):
    try:
        if protocol.upper() == "TCP":
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((ip, port))
            sock.close()
            return result == 0
        elif protocol.upper() == "UDP":
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.settimeout(1)
            sock.sendto(b'', (ip, port))
            try:
                data, addr = sock.recvfrom(1024)
            except socket.timeout:
                pass
            finally:
                sock.close()
            return True
        else:
            print(f"{colors['red']}[-]{colors['reset']}{colors['bold']} Protocolo não suportado: {protocol}{colors['reset']}")
            return False
    except Exception as e:
        print(f"{colors['red']}[-]{colors['reset']}{colors['bold']} Ocorreu um erro durante o scan de porta: {e}{colors['reset']}")
        return False

def main():
    banner = f"""{colors['purple']}
   ▄█   ▄█▄ ███▄▄▄▄    ▄██████▄   ▄████████  ▄█   ▄█▄ 
  ███ ▄███▀ ███▀▀▀██▄ ███    ███ ███    ███ ███ ▄███▀ 
  ███▐██▀   ███   ███ ███    ███ ███    █▀  ███▐██▀   
 ▄█████▀    ███   ███ ███    ███ ███       ▄█████▀    
▀▀█████▄    ███   ███ ███    ███ ███      ▀▀█████▄    
  ███▐██▄   ███   ███ ███    ███ ███    █▄  ███▐██▄   
  ███ ▀███▄ ███   ███ ███    ███ ███    ███ ███ ▀███▄ 
  ███   ▀█▀  ▀█   █▀   ▀██████▀  ████████▀  ███   ▀█▀ 
  ▀                                         ▀         
{colors['reset']}"""
    print(banner)

    if not sys.argv[1:] or "-h" in sys.argv[1:] or "--help" in sys.argv[1:]:
        print(f"{colors['yellow']}[*] Modo de uso:{colors['reset']}")
        print(f"  {colors['blue']}[+] Modo 1: {colors['reset']}{colors['bold']}Realizar batidas nas portas sem scan:{colors['reset']}")
        print(f"      {colors['yellow']}./knock.py HOST PORTA1 PROTOCOLO1 PORTA2 PROTOCOLO2 ...{colors['reset']}")
        print(f"      {colors['bold']}Exemplo: {colors['reset']}{colors['yellow']}. /knock.py 172.16.1.120 9090 TCP 8080 UDP 7070 TCP{colors['reset']}")
        print()
        print(f"  {colors['blue']}[+] Modo 2: {colors['reset']}{colors['bold']}Realizar batidas nas portas com scan em uma porta específica:{colors['reset']}")
        print(f"      {colors['yellow']}./knock.py HOST PORTA1 PROTOCOLO1 PORTA2 PROTOCOLO2 ... --scan PORTA SCAN_PROTOCOLO{colors['reset']}")
        print(f"      {colors['bold']}Exemplo: {colors['reset']}{colors['yellow']}. /knock.py 172.16.1.120 9090 TCP 8080 UDP 7070 TCP --scan 22 TCP{colors['reset']}")
        sys.exit()

    parser = argparse.ArgumentParser(description="Script de port knocking", add_help=False)
    parser.add_argument("host", nargs="?", help="O endereço IP do host")
    parser.add_argument("knocks", nargs="*", help="Pares de porta e protocolo para o port knocking")
    parser.add_argument("--scan", nargs=2, metavar=("PORTA", "PROTOCOLO"), help="Realizar um scan de porta após as batidas")
    args = parser.parse_args()

    for i in range(0, len(args.knocks), 2):
        port = int(args.knocks[i])
        protocol = args.knocks[i+1].upper()
        print(f"{colors['blue']}[+] Knocking{colors['reset']} {args.host} {port} {protocol}")
        if protocol == "TCP":
            knock_tcp(args.host, port)
        elif protocol == "UDP":
            knock_udp(args.host, port)
        time.sleep(1)

    if args.scan:
        port = int(args.scan[0])
        protocol = args.scan[1].upper()
        print(f"{colors['blue']}[+] Verificando estado da porta{colors['reset']} {args.host} {port} {protocol}")
        port_status = scan_port(args.host, port, protocol)
        if port_status:
            print(f"{colors['green']}[+] A porta {port} está aberta{colors['reset']}")
        else:
            print(f"{colors['red']}[-] A porta {port} está fechada{colors['reset']}")

if __name__ == "__main__":
    main()