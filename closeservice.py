#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Janice Cheng

import socket
ip_port = ('127.0.0.1',9999)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)


#s.bind(ip_port)





s.close()

