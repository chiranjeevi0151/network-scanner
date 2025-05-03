import os
import platform

def ping(ip):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = f"ping {param} 1 {ip}"
    return os.system(command) == 0

def scan_network():
    print("Scanning network...")
    network = "192.168.56.1" 
    for i in range(1, 255):
        ip = network + str(i)
        if ping(ip):
            print(f"Device found: {ip}")

scan_network()