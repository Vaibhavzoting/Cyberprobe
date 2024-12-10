import argparse
from modules.network_discovery import network_discovery
from modules.port_scanner import port_scanner
from modules.vulnerability_db import load_vulnerability_db, save_scan_profile, load_scan_profile
from modules.exploits import test_ftp_anonymous, test_http_traversal, test_smb_enumeration

def parse_arguments():
    parser = argparse.ArgumentParser(description="CyberProbe - A Simple Penetration Testing Tool")
    parser.add_argument('-t', '--target', type=str, required=True, help='Target IP Address')
    parser.add_argument('-p', '--ports', type=str, required=True, help='Port range (e.g., 80-100)')
    parser.add_argument('-e', '--exploits', type=str, help='Exploits to run (e.g., ftp,smb)')
    parser.add_argument('-d', '--discovery', action='store_true', help='Perform network discovery')
    
    args = parser.parse_args()
    return args

def main():
    args = parse_arguments()
    
    # Perform network discovery if the flag is provided
    if args.discovery:
        network_discovery(args.target)
    
    # Run port scanner with the specified target and port range
    if args.target and args.ports:
        start_port, end_port = map(int, args.ports.split("-"))
        vuln_db = load_vulnerability_db()
        port_scanner(args.target, (start_port, end_port))
        
    # Run exploits if specified
    if args.exploits:
        exploits = args.exploits.split(",")
        for exploit in exploits:
            if exploit == "ftp":
                print(test_ftp_anonymous(args.target))
            elif exploit == "http":
                print(test_http_traversal(args.target, 80))
            elif exploit == "smb":
                print(test_smb_enumeration(args.target))
    
    # Save scan profile if desired
    save_scan_profile("MyScanProfile", {"target_ip": args.target, "ports": args.ports})

if __name__ == "__main__":
    main()
