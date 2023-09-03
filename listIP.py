from scapy.all import *
from scapy.config import conf

print(get_if_list())
# packets = sniff(count = 5, iface = dev_from_index(2))
# print(packets[2][UDP])

def packet_handler(packet):
    print(packet.summary())

print(sniff(prn=packet_handler, iface=dev_from_index(3)))

# print(read_routes())
# id = 0
# for i in read_routes():
#     print("index: ",id+1," IP :",i[4])
#     id = id+1
# sniff(prn)
# nbPackets=int(input('Combien de paquet souhaitez-vous sniffer ?'))
# show_interfaces()
# indexCarte=int(input('Quel est l\'index de la carte à capturer  ?'))
# packets=sniff(count=nbPackets,iface=dev_from_index(indexCarte))
# listeIP=[]
# for packet in packets :
#     if packet.haslayer(IP) :
#         if packet[IP].src not in listeIP :
#             listeIP.append(packet[IP].src)
#         if packet[IP].dst not in listeIP :            
#             listeIP.append(packet[IP].dst)

# print(listeIP)

# with open("capture_stat_ip.csv","w") as fl:
#     for ip in listeIP:
#         fl.write(ip+'\n')

# nbPackets=int(input('Combien de paquet souhaitez-vous sniffer ?'))
# show_interfaces()
# indexCarte=int(input('Quel est l\'index de la carte à capturer  ?'))
# packets=sniff(count=nbPackets,iface=dev_from_index(indexCarte))
# fluxIP={}
# for packet in packets :
#     if packet.haslayer(IP) :
#         if packet[IP].src not in fluxIP :
#             fluxIP[packet[IP].src]=packet[IP].dst

# for srcIP in fluxIP:
#     print(srcIP+"->"+fluxIP[srcIP])

# from scapy.all import *
# packets=sniff(iface=dev_from_index(3))
# print(packets)

# from scapy.all import *
# listIP=[]
# show_interfaces()
# indexCarte=int(input('Quel est l\'index de la carte à capturer  ?'))
# def countIP(packet):
#     if packet.haslayer(IP):
#         if(packet[IP].src not in listIP):
#             listIP.append(packet[IP].src)
#         if(packet[IP].dst not in listIP):
#             listIP.append(packet[IP].dst)
# packets=sniff(iface=dev_from_index(indexCarte),prn=countIP)
# print(listIP)

# from scapy.all import *
# nbPackets=int(input('Combien de paquet souhaitez-vous sniffer ?'))
# coucheASniffer=input('Quelle couche souhaitez-vous capturer ?')
# show_interfaces()
# indexCarte=int(input('Quel est l\'index de la carte à capturer  ?'))
# packets=sniff(count=nbPackets,iface=dev_from_index(indexCarte))
# compteur=0
# for packet in packets :
#     if(packet.haslayer(coucheASniffer)):
#         compteur+=1

# print('La capture contient '+str(compteur)+' paquets du type '+coucheASniffer)

# from random import choices,randint
# show_interfaces()
# indexCarte=int(input('Quel est l\'index de la carte sur laquelle envoyer ?'))
# IPSRC='127.0.0.1'
# IPDST='127.0.0.1'
# while(1):
#     pktTCP=TCP(dport=53,sport=randint(1024,65536),seq=randint(0,65536))
#     pktIP=IP(src=IPSRC,dst=IPDST)
#     pktTCP_IP=pktIP/pktTCP
#     pktRAW=Raw(''.join([chr(x) for x in choices(range(0,256),k=randint(12,500))]))
#     pktDNS_TCP_IP=pktTCP_IP/pktRAW
#     send(pktDNS_TCP_IP,iface=dev_from_index(indexCarte))

# show_interfaces()
# indexCarte=int(input('Quel est l\'index de la carte à capturer  ?'))
# def checkDNS(pkt):
#     if(not pkt.haslayer(DNS)):
#         print('! ATTENTION PAQUET DNS MALFORME !')
#         print('Contenu du paquet :')
#         pkt.show()
# packets=sniff(iface=dev_from_index(indexCarte),prn=checkDNS,filter='tcp port 53')

# IPInterdites=['192.168.56.12','10.0.0.2','15.18.16.22']
# show_interfaces()
# indexCarte=int(input('Quel est l\'index de la carte à capturer  ?'))
# def filterIP(pkt):
#     if(pkt[IP].src in IPInterdites or pkt[IP].dst in IPInterdites):
#         print('! ATTENTION ADRESSE IP INTERDITE !')
#         print('Contenu du paquet :')
#         pkt.show()
# packets=sniff(iface=dev_from_index(indexCarte),prn=filterIP,filter='ip')

# IPAutorisees=['192.168.56.12','10.0.0.2','15.18.16.22','127.0.0.1']
# show_interfaces()
# indexCarte=int(input('Quel est l\'index de la carte à capturer  ?'))
# def filterIP(pkt):
#     if(pkt[IP].src not in IPAutorisees or pkt[IP].dst not in IPAutorisees):
#         print('! ATTENTION ADRESSE IP INTERDITE !')
#         print('Contenu du paquet :')
#         pkt.show()
# packets=sniff(iface=dev_from_index(indexCarte),prn=filterIP,filter='ip')

# from scapy.config import conf
# listProtos=[layer.__name__ for layer in conf.layers]
# nbPackets=int(input('Combien de paquet souhaitez-vous sniffer ?'))
# show_interfaces()
# indexCarte=int(input('Quel est l\'index de la carte à capturer  ?'))
# packets=sniff(count=nbPackets,iface=dev_from_index(indexCarte))
# nbPacketsByProtos={}
# for packet in packets:
#     for proto in listProtos:
#         if packet.haslayer(proto):
#             if proto in nbPacketsByProtos:
#                 nbPacketsByProtos[proto]+=1
#             else:            
#                 nbPacketsByProtos[proto]=1
# for proto in nbPacketsByProtos:
#     print(proto+';'+str(100*nbPacketsByProtos[proto]/nbPackets)+'%')