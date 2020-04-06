#!/usr/bin/env python
# coding: utf-8
# qpy:2
# erzeugt Montag, 06. April 2020 13:20 (C) 2020 von Leander Jedamus
# modifiziert Montag, 06. April 2020 13:29 von Leander Jedamus

from __future__ import print_function
import socket
import select

port = 50000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("", port))
server.listen(1)

clients = []

try:
  while True:
    lesen, schreiben, oob = select.select([server] + clients, [], [])
    
    for sock in lesen:
      if sock is server:
        client, addr = server.accept()
        clients.append(client)
        print("+++ Client {} verbunden".format(addr[0]))
      else:
        nachricht = sock.recv(1024)
        ip = sock.getpeername()[0]
        if nachricht:
          print("[{}] {}".format(ip, nachricht.decode()))
        else:
          print("+++ Verbindung zu {} beendet".format(ip))
          sock.close()
          clients.remove(sock)
finally:
  for c in clients:
    c.close()
  server.close()