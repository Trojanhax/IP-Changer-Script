import subprocess
import time
import random

# Network interface name (e.g., "Ethernet" or "Wi-Fi")
interface_name = "Wi-Fi"

while True:
    try:
        # Generate a random IP address (for demonstration purposes)
        new_ip = f"192.168.{random.randint(0, 255)}.{random.randint(0, 255)}"
        
        # Change the IP address using netsh
        subprocess.run(["netsh", "interface", "ip", "set", "address", interface_name, "static", new_ip, "255.255.255.0"])
        
        print(f"Changed IP address to {new_ip}")
        
        # Sleep for 5 seconds before changing again
        time.sleep(10)
    
    except KeyboardInterrupt:
        # Stop the script if Ctrl+C is pressed
        break
