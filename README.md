# PortIP

```
 _____           _   _____ _____  
 |  __ \         | | |_   _|  __ \ 
 | |__) |__  _ __| |_  | | | |__) |
 |  ___/ _ \| '__| __| | | |  ___/ 
 | |  | (_) | |  | |_ _| |_| |     
 |_|   \___/|_|   \__|_____|_|     
```

PortIP is a Python package that allows you to ping websites and scan for open ports. It is also available for Linux terminals.

## Installation

### Using pip

You can install this library using pip:

```bash
pip install portip
```

### Using apt-get (Linux)

To install PortIP on a Linux machine, use the following command:

```bash
sudo apt-get install portip
```

## Motive Of The Project

Network administrators and security enthusiasts often need a tool to quickly check the status of network services and open ports on a server. This can help in ensuring that only necessary services are exposed and identify potential vulnerabilities. As a network enthusiast myself, I developed this tool to make the process straightforward and efficient.

This package is designed to be easy to use, even for those who are not proficient in Python programming. By following a few simple steps, you can scan websites for open ports and check their connectivity.

## Structure Of The Project

```
portip/
│
├── portip/
│   ├── __init__.py
│   └── portip.py
│
├── CONTRIBUTING.md
├── LICENSE
├── README.md
└── setup.py
```

## Usage

After installing the package, create a new Python (.py) file in the same folder where you're working on your project.

Copy the following lines of code to your .py file:

```python
from portip.portip import ping_website, scan_all_ports

# Define the website URL
url = "YOUR_URL"

# Number of ping requests
num_requests = 4

# Ping the website
ping_website(url, num_requests)

# Resolve IP address
ip = socket.gethostbyname(url)

# Define the port range to scan
start_port = 1
end_port = 1024

# Scan ports
scan_all_ports(ip, start_port, end_port)
```

You just need to substitute `YOUR_URL` with the URL of the website you want to scan. This will ping the website and scan ports from 1 to 1024.

## Contribution

If you want to contribute to this project, please follow the instructions in the [CONTRIBUTING.md](https://github.com/PB2204/py-portip/blob/main/CONTRIBUTING.md)] file.

Happy Hacking! 🚀
