# !/usr/bin/env python
# -*- coding:utf-8 -*-
import dpkt
import binascii
from libs.c2utils import multibyte_xor
from libs.rc4 import rc4
from libs.b64 import b64decode


class pcaparser(object):
    @staticmethod
    def xor_example(tcp):
        if isinstance(tcp, dpkt.tcp.TCP):
            xor_key = 'a1a2a3a4'
            encrypted = binascii.b2a_hex(dpkt.http.Request(tcp.data).body)
            decrypt = multibyte_xor(encrypted, xor_key)
            print decrypt

    @staticmethod
    def rc4_example(tcp):
        if isinstance(tcp, dpkt.tcp.TCP):
            rc4_key = binascii.a2b_hex('a1a2a3a4')
            encrypted = tcp.data
            decrypt = rc4(rc4_key).crypt(encrypted)
            print decrypt

    @staticmethod
    def b64_example(tcp):
        if isinstance(tcp, dpkt.tcp.TCP):
            encrypted = tcp.data
            alpha = 'ZinaukMI9D5pzOG803hsRjNt/EBqVYKCXL+oxQTJc1dymHS4bFgl7UrWfP2v=we6'
            decrypt = b64decode(encrypted, alpha)
            print decrypt
