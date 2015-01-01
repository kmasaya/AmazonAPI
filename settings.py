#!/usr/bin/python3

import socket

LOCAL_HOST_NAME = '1280jp'

if socket.gethostname() == LOCAL_HOST_NAME:
    DEBUG = True
else:
    DEBUG = False
