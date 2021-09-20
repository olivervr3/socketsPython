import socket 
import threading
import PIL
from PIL import Image


HEADER = 64
PORT = 8010
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
FIN = "FIN"
MAX_CONEXIONES = 2

def handle_client(conn, addr):
    print(f"[NUEVA CONEXION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
        if msg == FIN:
            connected = False
        else:
            print(f" He recibido del cliente [{addr}] la imagen: {msg}")
            if msg == "PENGU":
                im = Image.open(r"/home/ovr3/Desktop/Include/images/PENGU.jpg")
                im.show()
                conn.send(f"ENHORABUENA! Se ha abierto la imagen {msg} en el servidor.".encode(FORMAT))
            elif msg == "UA":
                im = Image.open(r"/home/ovr3/Desktop/Include/images/UA.jpg")
                im.show()
                conn.send(f"ENHORABUENA! Se ha abierto la imagen {msg} en el servidor.".encode(FORMAT))
            elif msg == "PYTHON":
                im = Image.open(r"/home/ovr3/Desktop/Include/images/PYTHON.jpg")
                im.show()
                conn.send(f"ENHORABUENA! Se ha abierto la imagen {msg} en el servidor.".encode(FORMAT))
            else:
                conn.send(f"Imagen {msg} no existe pruebe otravez o salir escribiendo FIN.".encode(FORMAT))
    print("ADIOS. TE ESPERO EN OTRA OCASION")
    conn.close()
    server.close()
    
        

def start():
    server.listen()
    print(f"[LISTENING] Servidor a la escucha en {SERVER}")
    CONEX_ACTIVAS = threading.active_count()-1
    print(CONEX_ACTIVAS)
    while True:
        conn, addr = server.accept()
        CONEX_ACTIVAS = threading.active_count()
        if (CONEX_ACTIVAS <= MAX_CONEXIONES):
            conn.send(f"Buenos dias. El servidor dispone de estas imagenes:\n"
                 f"- PENGU \n"
                 f"- UA \n"
                 f"- PYTHON \n"
                 f"Cual quiere? \n"
                 f"(Para finalizar conexion escriba FIN)".encode(FORMAT))
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()
            print(f"[CONEXIONES ACTIVAS] {CONEX_ACTIVAS}")
            print("CONEXIONES RESTANTES PARA CERRAR EL SERVICIO", MAX_CONEXIONES-CONEX_ACTIVAS)
        else:
            print("OOppsss... DEMASIADAS CONEXIONES. ESPERANDO A QUE ALGUIEN SE VAYA")
            conn.send("OOppsss... DEMASIADAS CONEXIONES. Tendrás que esperar a que alguien se vaya".encode(FORMAT))
            conn.close()
            CONEX_ACTUALES = threading.active_count()-1
        

######################### MAIN ##########################


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

print("[STARTING] Servidor inicializándose...")

start()

