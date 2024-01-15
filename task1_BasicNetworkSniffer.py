from scapy.all import sniff, Ether, IP, TCP

def packet_callback(packet):
    if Ether in packet and IP in packet and TCP in packet:
        eth_header = packet[Ether]
        ip_header = packet[IP]
        tcp_header = packet[TCP]

        # Show or do what you want with headers
        print('\nEthernet Header:', eth_header.summary())
        print('IP Header:', ip_header.summary())
        print('TCP Header:', tcp_header.summary())

if __name__ == '__main__':
    # Using scapy for packet capture
    sniff(prn=packet_callback, store=0)
