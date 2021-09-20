import socket
import sys
import PIL
from PIL import Image

HEADER = 64
PORT = 8010
FORMAT = 'utf-8'
FIN = "FIN"

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)


if (len(sys.argv) == 3):
    SERVER = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (SERVER, PORT)

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    print(f"Establecida conexión en [{ADDR}]")
    print("Recibo del Servidor: ", client.recv(2048).decode(FORMAT))
    msg = input()
    while msg != FIN:
        print("Envio al servidor: ", msg)
        send(msg)
        im = Image.open(client.recv(2048).decode(FORMAT))
        im.show()
        msg = input()
    print("SE ACABO LO QUE SE DABA")
    print("Envio al servidor: ", FIN)
    send(FIN)
    client.close()
else:
    print("Oops!. Parece que algo falló. Necesito estos argumentos: <ServerIP> <Puerto> <Texto Bienvenida>")

