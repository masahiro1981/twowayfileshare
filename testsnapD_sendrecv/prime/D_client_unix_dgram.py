#!/usr/bin/python3

import os
import sys
import socket

def send_payload(socket_path):

    msg = "sendDDDDD"

    senddata = msg.encode()
    
    with socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.connect(socket_path)

        print("send() len={}, msg={} ----->".format(len(senddata), msg), flush=True)
        s.send(senddata)
        print("<----- send()", flush=True)



if __name__ == '__main__':
    # サーバ側に用意されるソケットファイルパスを指定
    socket_path = '/var/snap/testsnap-d-sendrecv/current/import/unix_socket_recvC'

    send_payload(socket_path)


