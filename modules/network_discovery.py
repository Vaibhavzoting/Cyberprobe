from scapy.all import ARP, Ether, srp

def network_discovery(target_ip):
    """Discover all devices on the local network."""
    print("\n[+] Performing network discovery...")
    target_ip = target_ip.split("/")[0]  # Remove subnet part (e.g., 192.168.1.0/24 -> 192.168.1.0)
    arp_request = ARP(pdst=target_ip + "/24")  # ARP request for the whole network
    ether_frame = Ether(dst="ff:ff:ff:ff:ff:ff")  # Broadcast frame
    request_packet = ether_frame/arp_request  # Combine both ARP and Ether layers
    
    result = srp(request_packet, timeout=3, verbose=False)[0]  # Send and receive packet
    
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})
    
    print("\n[+] Discovered Devices:")
    for device in devices:
        print(f"IP: {device['ip']} | MAC: {device['mac']}")
    
    return devices
