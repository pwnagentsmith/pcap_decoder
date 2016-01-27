Pcap Decoders
========

Packets Decoder Framework

What is pcap decoder
===========

This is a pcap decode framework that is similar to [chopshop](https://github.com/MITRECND/chopshop).

The limitation of chopshop is only work for complete session pcap to decrypt. Therefore, __pcap-decoder__ just use for-loop to parse all packets in the pcap file.

Usage
===========

	$ python pcap_decoder.py -f `[PCAP]` `[MODULE]`

Requirement
===========

pip install -r requirements.txt

Note
===========

All the library python codes in 'libs/' are from [chopshop](https://github.com/MITRECND/chopshop).
