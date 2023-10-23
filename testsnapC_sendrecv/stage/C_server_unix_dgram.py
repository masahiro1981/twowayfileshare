#!/usr/bin/python3

import os
import sys
import socket


def srv_sock_file():
    socket_path = '/var/snap/testsnap-c-sendrecv/current/export/unix_socket_recvC'
    datasize = 1024

    print("socket_path:{}".format(socket_path), flush=True)
#create a folder where socket will be created
    os.makedirs(os.path.dirname(socket_path), exist_ok=False)
    if os.path.exists(socket_path):
        os.remove(socket_path)

    try:
        with socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM) as s:
            s.bind(socket_path)

            while True:
                print("wait recv", flush=True)
                recvdata = s.recv(datasize)

                data = recvdata.decode()
                print("received : {}bytes.\ndata={}".format(len(recvdata), data), flush=True)

    except KeyboardInterrupt:
        print("KeyboardInterrupt", flush=True)

    finally:
        if os.path.exists(socket_path):
            os.remove(socket_path)


if __name__ == '__main__':
    srv_sock_file()

