# Cyberprobe

CyberProbe - Cybersecurity Tool
Overview
---------
CyberProbe is an all-in-one cybersecurity tool designed for penetration testing and vulnerability scanning. It is capable of scanning open ports, detecting vulnerabilities, and running exploits against known weaknesses in services like FTP and HTTP. It also features advanced reporting, real-time updates, and the ability to run multiple scans simultaneously using threading for faster results.

Features
1. Port Scanning: CyberProbe scans a given range of ports on a target IP address to determine which ports are open. It uses socket programming for efficient scanning and ThreadPoolExecutor to speed up the process with concurrent threads.

2.Vulnerability Detection:

 - FTP Anonymous Login: It detects whether the FTP server allows anonymous login, which could be a serious security risk.
 - HTTP Directory Traversal: It checks if the HTTP server is vulnerable to directory traversal attacks, allowing unauthorized access to sensitive files outside the web server’s root directory.

3. Exploit Testing: If vulnerabilities are found, CyberProbe can test known exploits. For example, it tests FTP servers for anonymous login and HTTP servers for directory traversal vulnerabilities.

4. Advanced Reporting: After completing a scan, CyberProbe generates a detailed report showing open ports and detected vulnerabilities. The tool also provides real-time progress via a tqdm progress bar.

5. Modular Design: The tool is organized into different modules, allowing for easier management of code, scalability, and the addition of more features in the future.

Technologies Used
Python: The primary language used for CyberProbe, leveraging Python’s simplicity and extensive library support.

Socket Programming: Used for the core functionality of scanning ports and testing network connectivity.

Threading (ThreadPoolExecutor): Used for concurrent scanning of multiple ports to speed up the scanning process.

tqdm: A library for creating progress bars to give real-time feedback during scans.

JSON: Used for storing configurations and vulnerabilities, which helps in easily updating and maintaining the tool.

Modules and Components
------------------------

CyberProbe is organized into different modules for better code organization:

port_scanner.py: Contains the logic for scanning ports and identifying open ports.
network_discovery.py: Can be used to discover other devices on the network.
vulnerability_db.py: A database for storing common vulnerabilities.
exploits.py: Contains known exploits that can be tested once vulnerabilities are detected.
cyberprobe.py: The main entry point for running the tool. It parses command-line arguments and orchestrates the different modules.

How to Operate the Tool
---------------------------
Step 1: Install Dependencies
-------
Ensure you have the necessary Python libraries installed. Run the following command to install the required dependencies:

bash Terminal
--------------
pip install tqdm

Step 2: Running the Tool
------
You can run CyberProbe from the command line by executing the main script cyberprobe.py. Here's the basic syntax:

bash
----
python cyberprobe.py -t <TARGET_IP> -p <START_PORT-END_PORT> [-e EXPLOIT_TYPE] [-d]

Command-Line Arguments
-----------------------
-t <TARGET_IP>: The target IP address you want to scan.
-p <START_PORT-END_PORT>: A range of ports to scan (e.g., 80-100).
-e EXPLOIT_TYPE: The type of exploit to test (optional). Example types are ftp or http.
-d: Enables debug output (optional, for development purposes).

Step 3: Example Command
To scan the ports from 80-100 on a target IP 10.10.252.44 and check for FTP and HTTP vulnerabilities:

bash
python cyberprobe.py -t 10.10.252.44 -p 80-100 -e ftp,http

Step 4: Viewing Results
------
After running the scan, the tool will output:

Open ports found in the range.
Vulnerabilities detected for FTP (anonymous login) or HTTP (directory traversal).
Exploit status if any exploits are tested.
Example output:

bash
------
Scanning ports 80-100 on 10.10.252.44...
[Scanning Ports] 100% |███████████████| Time: 0:02:03

[+] Open ports: [80, 443, 8080]
[+] FTP Exploit: Anonymous login detected! (Details...)
[+] HTTP Exploit: Directory traversal detected! (Details...)

Step 5: Mitigation Suggestions
------
If vulnerabilities are detected, the tool will also suggest ways to mitigate the issues:

FTP Anonymous Login: Disable anonymous login and set up authentication for FTP users.
HTTP Directory Traversal: Implement proper input validation and restrict access to sensitive files.

Step 6: Documentation and Reporting
------
CyberProbe provides an output of the findings. You can document and report the discovered vulnerabilities, such as FTP anonymous login or HTTP directory traversal. This can help in patching and improving the security posture of the target system.

Conclusion
----------
CyberProbe is a simple yet powerful tool designed to help in vulnerability scanning, exploitation testing, and reporting. It leverages Python's libraries for efficient networking tasks, concurrent port scanning, and real-time feedback. The tool is modular, allowing easy expansion, and is suited for both beginners and advanced penetration testers.

File Structure
To keep everything organized, here's how the project directory should look:

CyberProbe/
│
├── modules/
│   ├── port_scanner.py  # Handles port scanning
│   ├── network_discovery.py  # For network discovery
│   ├── vulnerability_db.py  # Stores known vulnerabilities
│   ├── exploits.py  # Known exploits
│
├── cyberprobe.py  # Main script for running the tool
├── scan_profiles.json  # Configuration file for profiles
└── vulnerability_db.json  # Database of vulnerabilities

Further Development
This tool is just the beginning, and additional features can be added:

Integration with external vulnerability databases (e.g., CVE).
GUI (Graphical User Interface) for easier use.
Automated patching or remediation features.

Acknowledgments
---------------
CyberProbe was designed with simplicity and efficiency in mind, using Python for flexibility and ease of use. If you find bugs or have suggestions for new features, feel free to contribute to the development!


