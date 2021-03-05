from scapy.all import *
from scapy.layers.inet import IP
from scapy.utils import RawPcapReader

import pickle

def ipCapture(numPackets):
    packets = sniff(count=numPackets)
    return packets

def ip_src_dst(packets):  # Returns two lists, one of the packet capture's source and the other of the destination
    i = 0;
    ip_src = list()
    ip_dst = list()

    for packet in packets:
        if packet.haslayer(IP):
            ip_src.append(packets[i][IP].src)
            ip_dst.append(packets[i][IP].dst)
            i += 1
    return ip_src, ip_dst


def print_src_dst(ipsrc, ipdst):  # spews out all IP sources and destinations found in the given lists
    i = 0
    for output1 in ipsrc:
        print("IP source: " + ipsrc[i] + " IP destination: " + ipdst[i] + '\n')
        i += 1


def save_packets(numPackets):
    packets = sniff(count=numPackets)
    print ("What would you like to name the file (extension will always be .obj)? ")
    filename = input()
    filename = str(filename) + ".obj"
    print("file name will be: " + filename)
    file_packets = open(filename, 'wb')
    pickle.dump(packets, file_packets)

