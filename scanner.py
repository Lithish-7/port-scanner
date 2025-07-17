import socket
from datetime import datetime

# Banner
print("="*40)
print("      Simple Python Port Scanner")
print("="*40)

# Input
target = input("Enter target IP or domain: ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

print(f"\nScanning {target} from port {start_port} to {end_port}...\n")
start_time = datetime.now()

# Scan loop
for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"[+] Port {port} is open")
    sock.close()

# Timing
end_time = datetime.now()
print(f"\nScan completed in: {end_time - start_time}")
