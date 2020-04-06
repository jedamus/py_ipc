#!/usr/bin/env python
# coding: utf-8
# qpy:2
# erzeugt Montag, 06. April 2020 13:20 (C) 2020 von Leander Jedamus
# modifiziert Montag, 06. April 2020 13:26 von Leander Jedamus

from __future__ import print_function
import socket

port = 50000

ip = raw_input("IP-Adresse: ")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))

try:
  while True:
    nachricht = raw_input("Nachricht: ")
    s.send(nachricht.encode())
finally:
  s.close()
