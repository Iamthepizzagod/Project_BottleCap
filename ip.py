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


def save_packets_live(numPackets): #cpatures live packets and then saves them
    packets = sniff(count=numPackets)
    save_object(packets)

def save_object(object): #saves a static object of any kind as a .obj
    print("What would you like to name the file (extension will always be .obj)? ")
    filename = input()
    filename = str(filename) + ".obj"
    print("file name will be: " + filename)
    file_packets = open(filename, 'wb')
    pickle.dump(object, file_packets)

def pcapImport(pcapName):
    option = "0"
    # todo: add logic to make sure file + file name is a valid .pcap

    packets = sniff(offline=pcapName)
    #packets[0].show() #debug line, dosent seem to work on different indicies...

    while option != "n" and option != "y":
        print("Would you like to save the pcap output to a pickle file?(y/n) ")
        option = input()
        if option == "y":
            save_object(packets)

    packets.summary()
    return packets


def outputPktSummary(packets):
    y = 0;
    for i in packets:
        i.summary()
        y+=1
