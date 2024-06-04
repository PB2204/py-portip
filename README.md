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

## Usage (Windows Terminal / MAC Terminal)

After installing the package, you can use the following commands in your terminal or command prompt:

#### Ping a Website:

To ping a website and check its connectivity, use the following command:

```bash
python3 -m portip.portip 1 --url google.com
```

This command will ping `google.com` with the default number of requests (4 by default).

#### Scan for Open Ports:

To scan a website for open ports, use the following command:

```bash
python3 -m portip.portip 2 --url google.com
```

This command will scan `google.com` for open ports using the default settings (scanning ports 1 to 1000 with 100 threads).

#### Advanced Scanning Features:

You can enable advanced scanning features to improve port scanning accuracy. Use the `--advanced` flag with the scan command:

```bash
python3 -m portip.portip 2 --url google.com --advanced
```

This command will enable advanced scanning features while scanning `google.com` for open ports.

#### Specify Port Range:

If you want to specify a custom port range (e.g., ports 1-1000), use the `--port-range` option:

```bash
python3 -m portip.portip 2 --url google.com --port-range 1-1000
```

This command will scan `google.com` for open ports within the specified port range.

#### Adjust Number of Threads:

To change the number of threads used for port scanning, use the `--threads` option:

```bash
python3 -m portip.portip 2 --url google.com --threads 50
```

This command will scan `google.com` for open ports using 50 threads instead of the default 100.

Replace `google.com` with the URL of the website you want to ping or scan. Adjust the command-line options as needed to customize the behavior of the PortIP tool.

Feel free to reach out if you have any questions or encounter any issues!

## Usage (Linux Terminal)

After installing the package, you can use the following commands in your terminal or command prompt:

### Additional Setup on Linux

Before using the `portip` command, you need to ensure that the `portip.py` script is properly configured for use on a Linux machine.

1. **Install `dos2unix`**:
   If you haven't already installed `dos2unix`, you can do so using the following command:
   ```bash
   sudo apt-get install dos2unix
   ```

2. **Convert Line Endings**:
   Navigate to the directory containing `portip.py` and run the following command to convert the line endings of the script file to Unix-style:
   ```bash
   dos2unix portip.py
   ```

   This command ensures that the script can be executed properly on a Linux machine.

### Using the `portip` Command

#### Ping a Website:

To ping a website and check its connectivity, use the following command:
```bash
portip 1 --url google.com
```
This command will ping `google.com` with the default number of requests (4 by default).

#### Scan for Open Ports:

To scan a website for open ports, use the following command:
```bash
portip 2 --url google.com
```
This command will scan `google.com` for open ports using the default settings (scanning ports 1 to 1000 with 100 threads).

#### Advanced Scanning Features:

To enable advanced scanning features while scanning for open ports, use the `--advanced` flag:
```bash
portip 2 --url google.com --advanced
```
This command will enable advanced scanning features while scanning `google.com` for open ports.

#### Specify Port Range:

To specify a custom port range (e.g., ports 1-1000) for scanning, use the `--port-range` option:
```bash
portip 2 --url google.com --port-range 1-1000
```
This command will scan `google.com` for open ports within the specified port range.

#### Adjust Number of Threads:

To change the number of threads used for port scanning, use the `--threads` option:
```bash
portip 2 --url google.com --threads 50
```
This command will scan `google.com` for open ports using 50 threads instead of the default 100.

Replace `google.com` with the URL of the website you want to ping or scan. Adjust the command-line options as needed to customize the behavior of the PortIP tool.

Feel free to reach out if you have any questions or encounter any issues!

## Contribution

If you want to contribute to this project, please follow the instructions in the [CONTRIBUTING.md](https://github.com/PB2204/py-portip/blob/main/CONTRIBUTING.md) file.

Happy Hacking! 🚀