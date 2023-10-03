#!/usr/bin/python3

import os
import sys
import socket


def srv_sock_file():
    #socket_path = '/var/snap/testsnap-d-sendrecv/current/export/unix_socket_recvD'
    socket_path = '/home/masahiro/socktest/unix_socket_recvD'
    
    datasize = 1024

    print("socket_path:{}".format(socket_path), flush=True)

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

