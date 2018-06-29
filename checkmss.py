#!/usr/bin/python3

import socket
import sys
import struct
import argparse

parser = argparse.ArgumentParser(description='checkmss')
parser.add_argument(dest='hostname', metavar='HostName')
parser.add_argument(dest='port', metavar='TcpPort', type=int)

group = parser.add_mutually_exclusive_group()
group.add_argument("-4", '--ipv4', action="store_true", default=True)
group.add_argument("-6", '--ipv6', action="store_true")

args = parser.parse_args()

if args.ipv6:
    s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    f='ipv6'
else:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    f='ipv4'

s.settimeout(2)

try:
    s.connect((args.hostname, args.port))
except:
    sys.exit(0)

fmt = "B"*7+"I"*21
x = struct.unpack(fmt, s.getsockopt(socket.IPPROTO_TCP, socket.TCP_INFO, 92))
#print (x)
print (args.hostname, f, x[9], x[26])

