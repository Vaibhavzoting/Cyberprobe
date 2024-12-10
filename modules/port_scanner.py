import socket
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

def scan_port(target_ip, port):
    """Scan a single port and return whether it's open or closed."""
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set timeout to 1 second
        
        # Try to connect to the target IP and port
        result = sock.connect_ex((target_ip, port))
        
        # If result is 0, it means the port is open
        if result == 0:
            return port  # Port is open
        else:
            return None  # Port is closed
    except socket.error:
        return None  # In case of an error, assume port is closed
    finally:
        sock.close()  # Always close the socket

def port_scanner(target_ip, port_range):
    """Scan a range of ports on the target IP and print the open ones."""
    open_ports = []  # List to store open ports
    start_port, end_port = port_range
    
    print(f"Scanning ports {start_port}-{end_port} on {target_ip}...")
    
    # Use ThreadPoolExecutor to scan ports concurrently
    with ThreadPoolExecutor(max_workers=50) as executor:
        # Create a list of future tasks
        futures = [executor.submit(scan_port, target_ip, port) for port in range(start_port, end_port + 1)]
        
        # Progress bar for the port scan
        for future in tqdm(futures, desc="Scanning Ports", total=len(futures)):
            result = future.result()
            if result:
                open_ports.append(result)  # If port is open, add it to the list
    
    # Output the result
    if open_ports:
        print(f"\n[+] Open ports: {open_ports}")
    else:
        print("\n[-] No open ports found.")
