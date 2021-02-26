#! /usr/bin/env python3

from scapy.all import *
from scapy.layers.inet import IP, ICMP

i = 0;
packets = sniff(count=10)

for packet in packets:
    if packet.haslayer(IP):
        IPDst = packets[i][IP].dst;
        print("IP Destination is: " + IPDst + '\n ')
        i += 1




