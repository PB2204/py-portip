import socket
import threading
import argparse
import os
import platform
from queue import Queue
import datetime

# Number of threads for scanning
N_THREADS = 100
q = Queue()

# Function to grab the banner of the open port
def grab_banner(ip, port):
    try:
        s = socket.socket()
        s.connect((ip, port))
        s.settimeout(2)
        banner = s.recv(1024).decode().strip()
        print(f"[+] Banner on port {port}: {banner}")
        s.close()
    except:
        pass

# Function to get port type
def get_port_type(port):
    port_types = {
        21: "FTP",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        443: "HTTPS",
        3306: "MySQL",
        5432: "PostgreSQL",
        8080: "HTTP-Proxy"
        # Add more port types as needed
    }
    return port_types.get(port, "Unknown")

# Function to scan a specific port
def scan_port(ip, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)
    try:
        scanner.connect((ip, port))
        port_type = get_port_type(port)
        print(f"[+] Port {port} is open on {ip} - {port_type}")
        grab_banner(ip, port)
    except:
        pass
    finally:
        scanner.close()

# Worker thread function to get ports from the queue and scan them
def worker(ip):
    while True:
        port = q.get()
        scan_port(ip, port)
        q.task_done()

# Function to scan all ports
def scan_all_ports(ip, start_port, end_port):
    for port in range(start_port, end_port + 1):
        q.put(port)
    
    for _ in range(N_THREADS):
        thread = threading.Thread(target=worker, args=(ip,))
        thread.daemon = True
        thread.start()

    q.join()

# Function to ping a website with a specified number of requests
def ping_website(url, num_requests):
    try:
        target_ip = socket.gethostbyname(url)
        print(f"Resolved IP address for {url}: {target_ip}")
        
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        command = f"ping {param} {num_requests} {target_ip}"
        os.system(command)
    except socket.gaierror:
        print("Error: Could not resolve the IP address for the given URL.")

# Function to display the banner
def display_banner():
    banner = '''
  _____           _   _____ _____  
 |  __ \         | | |_   _|  __ \ 
 | |__) |__  _ __| |_  | | | |__) |
 |  ___/ _ \| '__| __| | | |  ___/ 
 | |  | (_) | |  | |_ _| |_| |     
 |_|   \___/|_|   \__|_____|_|     
    '''
    print(banner)
    print("\nWelcome to PortIP Scanner!\n")
    print("This tool allows you to:\n1. Ping a website to check connectivity.\n2. Scan for IP and open ports of a website.\n")

if __name__ == "__main__":
    display_banner()

    parser = argparse.ArgumentParser(description="Simple IP and Port Scanner")
    parser.add_argument("option", type=int, choices=[1, 2], help="Choose an option (1 or 2)")
    parser.add_argument("--url", type=str, help="URL to scan (e.g., google.com)")
    parser.add_argument("--threads", type=int, default=100, help="Number of threads to use")
    parser.add_argument("--port-range", type=str, help="Port range to scan (e.g., 1-1024)")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    if args.option == 1:
        url = args.url
        num_requests = int(input("Enter the number of ping requests: "))
        ping_website(url, num_requests)
    elif args.option == 2:
        url = args.url
        if args.url:
            try:
                target_ip = socket.gethostbyname(url)
                print(f"Resolved IP address for {url}: {target_ip}")

                # Update the number of threads if provided
                if args.threads:
                    N_THREADS = args.threads

                # Parse port range if provided
                if args.port_range:
                    start_port, end_port = map(int, args.port_range.split('-'))
                else:
                    start_port, end_port = 1, 1000  # Scanning only the first 1000 ports by default

                print(f"Scanning ports {start_port}-{end_port} on {target_ip} with {N_THREADS} threads...")
                scan_all_ports(target_ip, start_port, end_port)

                print("Scanning complete.")
                print(f"Scan date and time: {datetime.datetime.now()}")
            except socket.gaierror:
                print("Error: Could not resolve the IP address for the given URL.")
        else:
            print("Error: Please provide a valid URL.")
    else:
        print("Invalid option. Please choose 1 or 2.")