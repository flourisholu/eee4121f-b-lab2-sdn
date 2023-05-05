
from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
from pox.lib.util import dpidToStr
from pox.lib.addresses import EthAddr
from collections import namedtuple
import os
# TODO Add your imports here 
import csv


log = core.getLogger()
# policyFile = "%s/pox/pox/misc/firewall-policies.csv" % os.environ[ 'HOME' ]
policyFile = "%s/p4/eee4121f-b-lab2-sdn/firewall/firewall-policies.csv" % os.environ[ 'HOME' ]

#TODO Add your global variables here 
blocked_hosts = []

with open(policyFile) as data:
    read = csv.reader(data)
    next(read)
    for i in read:
        blocked_hosts.append(i[1])

    # Vary the number of blocked hosts
    # blocked_hosts = blocked_hosts[:-2] #1, 2, 3

class Firewall (EventMixin):

    def __init__ (self):
        self.listenTo(core.openflow)
        log.debug("Enabling Firewall Module")

    def _handle_ConnectionUp (self, event):
        #TODO Add your logic here 



        log.debug("Firewall rules installed on %s", dpidToStr(event.dpid))

def launch ():
    #    Starting the Firewall module
    
    core.registerNew(Firewall)
