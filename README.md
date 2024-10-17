# Port Scanner

## Overview
This project is a simple TCP port scanner built using Python's `socket` and `threading` libraries. It scans a given target IP address for open ports, which is a common network security technique.

## Features
- **TCP Port Scanning**: Scans specific or ranges of TCP ports on a target machine.
- **Multithreading**: Scans multiple ports simultaneously using multiple threads for faster results.

## How to Use

1. Run the script:
```bash
python3 port_scanner.py
```

## Expected Output

```bash
Enter the target IP address: 192.168.1.1
Resolved target IP: 192.168.1.1
Scan a range of ports or specific ports? (r/s): r
Enter the starting port number: 20
Enter the ending port number: 80
Scanning 192.168.1.1 for open ports from 20 to 80...
Port 22 is OPEN
Port 80 is OPEN
Port 21 is CLOSED
...
```
