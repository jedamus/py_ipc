#!/usr/bin/env python
# coding: utf-8
# qpy:2
# erzeugt Montag, 06. April 2020 13:20 (C) 2020 von Leander Jedamus
# modifiziert Donnerstag, 03. Dezember 2020 20:36 von Leander Jedamus
# modifiziert Montag, 06. April 2020 15:41 von Leander Jedamus

from __future__ import print_function
import sys
import socket

if int(sys.version_info.major) < 3:
  my_input = raw_input
else:
  my_input = input

port = 50000

ip = my_input("IP-Adresse: ")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))

try:
  while True:
    nachricht = my_input("Nachricht: ")
    if nachricht == "ende":
      break
    s.send(nachricht.encode())
finally:
  s.close()
