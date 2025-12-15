import socket

print("Target Website (e.g., google.com):")
target = input()

# 1. Get the IP Address (The House Address)
target_ip = socket.gethostbyname(target)
print("-" * 50)

# 2. Define the specific doors we want to knock on
# Port 80 = Web, Port 443 = Secure Web, Port 22 = SSH
ports_to_scan = [80, 443, 22, 21]

print("Starting Scan... please wait...")

# 3. The Loop (knocking on each door)
for port in ports_to_scan:
    # Create a socket (a phone line)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # set a timeout so we don't wait forever
    s.settimeout(1)

    # Try to connect (Knock on the door)
    # connect_ex returns 0 if the door is OPEN
    result = s.connect_ex((target_ip, port))

    if result == 0:
        print(f"Port {port}: OPEN [!!!]")
    else:
        print(f"Port {port}: Closed")

    s.close() # Hang up the phone

print("Scan Complete.")
