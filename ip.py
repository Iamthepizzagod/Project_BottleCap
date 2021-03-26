from scapy.all import *
from scapy.layers.inet import IP

import helperFuncs as helper


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


def save_packets_live(numPackets):  # cpatures live packets and then saves them
    packets = sniff(count=numPackets)
    save_object(packets)


def pcapImport(pcapName):
    option = "0"
    packets = None

    try:
        packets = sniff(offline=pcapName)
    except:
        print("File not valid.")
    packets[0].show()  # debug line, dosent seem to work on different indicies sometimes...

    if packets is not None:
        while option != "n" and option != "y" and packets is not None:
            print("Would you like to save the pcap output to a pickle file?(y/n) ")
            option = input()
            if option == "y":
                save_object(packets)
        # packets.summary()

    return packets


def outputPktSummary(packets):
    y = 0;
    for i in packets:
        i.summary()
        y += 1


def ttlMain():
    userchoice = '0'
    while userchoice != 'a' and userchoice != 'b' and userchoice != 'c':
        print("Choose the following options for ttl analysis:\n"
              "a. Live ttl analysis\n"
              "b. Pcap analysis\n "
              "c. Scapy obj file analysis")
        userchoice = input()

    switcher = {
        'a': liveTTL,
        'b': pcapTTL,
        'c': objTTL
    }

    packets = switcher[userchoice]()

    try:
        ttlInfo = getTTL(packets)
        ips = ip_src_dst(packets)
        ip_src = ips[0]
        ip_dst = ips[1]

        i = 0
        for ttl in ttlInfo:
            print("TTL: " + str(ttl) + ", IP source: " + str(ip_src[i]) + ", IP Destination: " + str(ip_dst[i]))
            i += 1

        ttlAnalysis(ttlInfo, ip_src, ip_dst)
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")


def liveTTL():
    packetNumber = ''

    while type(packetNumber) is not int:
        print("Please input a valid number of packets to capture live:")
        try:
            packetNumber = int(input(), base=10)
        except:
            print("Oops!", sys.exc_info()[0], "occurred.")

    try:
        packets = ipCapture(packetNumber)
        return packets
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")


def pcapTTL():
    usrInput = 0
    while type(usrInput) is not str:
        print("Please type the name of the pcap file you wish to display TTL information on(case sensitive):")
        usrInput = input()

    return pcapImport(usrInput)


def objTTL():
    print("objTTL works")


def getTTL(packets):
    i = 0
    ttl = list()
    for packet in packets:
        if packet.haslayer(IP):
            ttl.append(packet[IP].ttl)
            i += 1
    return ttl


def ttlAnalysis(ttlInfo, ip_src, ip_dst):
    # dictionary analysis looks as follows: dict(ip_dst, dict(ttl, timesFound(int)))

    ttlAnalysis = dict()
    ttlFreq = dict()
    ttl_and_ipdst = dict()
    ip_dst_freq = helper.generic_freq(ip_dst)

def ip_dst_freq(ip_dst):
    ip_dst_freq = dict()

    i = 0
    for ip in ip_dst:
        if ip in ip_dst_freq:
            ip_dst_freq[ip] += 1
        else:
            ip_dst_freq[ip] = 1

    for key, value in ip_dst_freq.items():
        print(f"IP destination '{key}' shows up {value} times.")

    return ip_dst_freq