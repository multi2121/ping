import subprocess
import ipaddress
import socket  # for making a successful connection to the host
import sys  # for getting arguments input by the user.
from datetime import datetime
def ping_test (subnet):

    reached = []                           #Empty list to collect reachable hosts
    not_reached = []                          #Empty list to collect unreachable hosts

    for ip in subnet:
        f = open("log.txt", "a")
        ping_test = subprocess.call('ping %s -n 2' % ip, stdout=f)
        f.close()
    #Ping host n times
        if ping_test == 0:                    #If ping test is 0, it' reachable
            print (str(ip) + " reachable")
            reached.append(ip)

        else:
            print(str(ip) + " unreachable")
            not_reached.append(ip)                              #Else, it's not reachable

    print("{} is reachable".format(reached))
    print("{} not reachable".format(not_reached))

print (sys.argv)
if '0/' in sys.argv[1]:
    # handle CIDR
    print (ipaddress.IPv4Network(sys.argv[1]))

    ping_test (ipaddress.IPv4Network(sys.argv[1]))
