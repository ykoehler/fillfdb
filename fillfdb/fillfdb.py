from scapy.all import *
import click
import random

SELF_MAC = '02:02:02:02:02:02'    # fill in with your MAC address
BCAST_MAC = 'ff:ff:ff:ff:ff:ff'

def create_ARP_request_gratuituous(mac, ipaddr):
    arp = ARP(psrc=ipaddr,
              hwsrc=mac,
              pdst=ipaddr)
    return Ether(src=mac, dst=BCAST_MAC) / arp
    
@click.command()
@click.option("--count", "-c", "count", default=1, help="Number of gratuituous ARP to send.")
@click.option("--iface", "-i", "iface", required=True, help="Network Interface to send the packet over.")
def broadcast(count, iface):
    for i in range(count):
        mac = '00:24:' + hex(random.randint(0x10, 0x6f)).lstrip('0x') + ':' + hex(random.randint(0x10, 0x6f)).lstrip('0x') + ':' + hex(random.randint(0x10, 0x6f)).lstrip('0x') + ':' + hex(random.randint(0x10, 0x6f)).lstrip('0x')
        ipaddr = '10.0.0.' + str(random.randint(150,160))
        print("Sending packet with mac " + mac + " and ip " + ipaddr + "on the Network Interfae " + iface)

        sendp(create_ARP_request_gratuituous(mac, ipaddr), iface=iface)

if __name__ =="__main__":
    broadcast()