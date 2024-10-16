import socket
import threading

# Function to scan a single port
def scan_port(ip, port):
    try:
        # Create a socket (IPv4, TCP)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set timeout for socket connection attempts
        sock.settimeout(1)
        
        # Try to connect to the port
        result = sock.connect_ex((ip, port))
        
        # If the port is open, result will be 0
        if result == 0:
            print(f"Port {port} is OPEN")
        else:
            print(f"Port {port} is CLOSED")
        
        # Close the socket
        sock.close()
    
    except socket.error as err:
        print(f"Socket error: {err}")
        return

# Function to scan a range of ports
def scan_ports(ip, start_port, end_port):
    print(f"Scanning {ip} for open ports from {start_port} to {end_port}...")
    
    for port in range(start_port, end_port + 1):
        scan_port(ip, port)

# Function for multithreaded port scanning
def multithreaded_scan(ip, ports, num_threads=10):
    def thread_function(port_list):
        for port in port_list:
            scan_port(ip, port)

    # Split the port list into chunks for each thread
    chunk_size = len(ports) // num_threads
    threads = []
    
    for i in range(num_threads):
        start_index = i * chunk_size
        end_index = start_index + chunk_size if i != num_threads - 1 else len(ports)
        thread_ports = ports[start_index:end_index]
        
        thread = threading.Thread(target=thread_function, args=(thread_ports,))
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()

# Main function
if __name__ == "__main__":
    target_ip = input("Enter the target IP address: ")
    
    try:
        # Get the target's host name and IP address
        target_host = socket.gethostbyname(target_ip)
    except socket.error:
        print("Unable to resolve host")
        exit()

    print(f"Resolved target IP: {target_host}")
    
    # Option to scan a range of ports or specific ports
    scan_option = input("Scan a range of ports or specific ports? (r/s): ").lower()

    if scan_option == 'r':
        start_port = int(input("Enter the starting port number: "))
        end_port = int(input("Enter the ending port number: "))
        scan_ports(target_host, start_port, end_port)
    
    elif scan_option == 's':
        ports = input("Enter specific ports (comma-separated): ")
        ports = [int(port.strip()) for port in ports.split(",")]
        multithreaded_scan(target_host, ports)
    
    else:
        print("Invalid option!")
