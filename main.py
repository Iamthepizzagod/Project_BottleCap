#! /usr/bin/env python3
import argparse
import json
import os
import sys

import ip as bottleIP


def main():
    program = build_parser()
    main_menu(program)


def build_parser():  # function that builds all the argument/parser lists
    parser = argparse.ArgumentParser(description='Test program for packet captures.')
    parser.add_argument("--echo", help="prints out the string you put in")
    parser.add_argument("--packetCapture", help="Capture x amount of packets and save them in a pickle object.",
                        type=int)
    parser.add_argument("--printIP", help="Prints out source and destination IPs for x amount of IPs", type=int)
    parser.add_argument("--pcapImport", help="Reads in a pcap file as a packet list.", type=str)
    return parser


def main_menu(program):
    quitchar = "0"

    while quitchar != "y":
        args = program.parse_args()
        quitchar = "0"

        if args.printIP is not None:
            packets = bottleIP.ipCapture(args.printIP)
            ip_src_dst = bottleIP.ip_src_dst(packets)
            bottleIP.print_src_dst(ip_src_dst[0], ip_src_dst[1])
            packets[1].show()

        elif args.packetCapture is not None:
            bottleIP.save_packets(args.packetCapture)

        elif args.echo is not None:
            print(args.echo)

        elif args.pcapImport is not None:
            print(args.pcapImport)
            packets = bottleIP.pcapImport(args.pcapImport)

        while quitchar != "n" and quitchar != "y":
            print("Would you like to quit the program?(y/n) ")
            quitchar = input()


if __name__ == '__main__':
    main()
