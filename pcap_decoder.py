# !/usr/bin/env python
# -*- coding:utf-8 -*-
import dpkt
import argparse
from modules.parser import pcaparser


def open_pcap(pcap_file, module):
    with open(pcap_file, 'r') as f:
        pcap = dpkt.pcap.Reader(f)
        for ts, buff in pcap:
            eth = dpkt.ethernet.Ethernet(buff)
            ip = eth.data
            tcp = ip.data
            getattr(pcaparser, module)(tcp)


def main():
    parser = argparse.ArgumentParser(description='Pcap decoder')
    parser.add_argument('-f', dest='file',
                        metavar='FILE',
                        help='input pcap file')
    parser.add_argument('module',
                        metavar='MODULE',
                        help='module name')
    args = parser.parse_args()
    if args.file and args.module:
        open_pcap(args.file, args.module)

if __name__ == '__main__':
    main()
