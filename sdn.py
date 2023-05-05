#!/usr/bin/python

# EEE4121F-B Lab 2
# SDN

# Implementing a Layer-2 Firewall using POX and Mininet


from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def treeTopo():
    net = Mininet( controller=RemoteController )
    
    # Create the controller object and connect it to the network
    net.addController('c0')

    # Create 8 hosts objects and add them to the network
    hosts = []

    for i in range(8):
        hosts.append(net.addHost('h%s' % (i+1), ip='10.0.0.%s' % (i+1), mac='00:00:00:00:00:0%s' % (i+1)))

    # Create 7 switch objects and add them to the network
    switches = []

    for i in range(7):
        switches.append(net.addSwitch('s%s' % (i+1)))

    # Finally, create the links as described in the figure
    # Links between switches - this is a layer-2 SDN firewall
    root = s1
    layer_1 = [s2, s5]
    layer_2 = [s3, s4, s6, s7]
    
    for i, layer in enumerate(layer_1):
        net.addLink(root, layer)
        net.addLink(layer, layer_2[2*i])
        net.addLink(layer, layer_2[2*i+1])

    # Host links
    net.addLink(h1, s3)
    net.addLink(h2, s3)
    net.addLink(h3, s4)
    net.addLink(h4, s4)
    net.addLink(h5, s6)
    net.addLink(h6, s6)
    net.addLink(h7, s7)
    net.addLink(h8, s7)

    # Start the mininet network, start the CLI interface, and stop the mininet network 
    info('*** Starting network \n')
    net.start()

    info('*** Running CLI \n')
    CLI(net)
    net.pingAll()

    info('*** Stopping network \n')
    net.stop()   
    
    time.sleep(30)
    cleanup()

if __name__ == '__main__':
    setLogLevel( 'info' )
    treeTopo()
