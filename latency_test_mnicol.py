import socket
import time

print("Target to Ping (e.g., google.com):")
target = input()
port = 80  # We will knock on the front door

print(f"Checking speed to {target}...")

# 1. Start the Stopwatch
start_time = time.time()

# 2. Do the work (Connect to the server)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((target, port)) # This is the actual travel time
s.close()

# 3. Stop the Stopwatch
end_time = time.time()

# 4. Calculate the difference
duration = end_time - start_time

print(f"Raw Time: {duration} seconds")

# Make it look cool (Convert to milliseconds)
ms = round(duration * 1000, 2)
print("-" * 30)
print(f"LATENCY: {ms} ms")
print("-" * 30)

if ms < 50:
    print("STATUS: GOD SPEED")
elif ms < 150:
    print("STATUS: DECENT")
else:
    print("STATUS: TRASH CONNECTION")
