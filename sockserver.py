#!/usr/bin/env python
# coding: utf-8
# qpy:2
# erzeugt Montag, 06. April 2020 13:45 (C) 2020 von Leander Jedamus
# modifiziert Montag, 06. April 2020 13:29 von Leander Jedamus

from __future__ import print_function
import socketserver

class sockserver(socketserver.BaseRequestHandler):

  def handle(self):
    addr = self.client_address[0]
    print("[{}] Verbindung hergestellt".format(addr))
    while True:
      s = self.request.recv(1024)
      if s:
        print("[{}] {}".format(addr, s.decode()))
      else:
        print("[{}] Verbindung geschlossen".format(addr))
        break

def main():
  port = 50000
  server = socketserver.ThreadingTCPServer(("", port),
              socketserver)
  server.serve_forever()

if __name__ == "__main__":
  main()