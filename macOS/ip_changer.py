import subprocess
import time
import random

# Network interface name (e.g., "en0" for Ethernet or "en1" for Wi-Fi)
interface_name = "en0"

while True:
    try:
        # Generate a random IP address (for demonstration purposes)
        new_ip = f"192.168.{random.randint(0, 255)}.{random.randint(0, 255)}"
        
        # Set the new IP address using networksetup
        subprocess.run(["sudo", "networksetup", "-setmanualwithdhcprouter", interface_name, new_ip])
        
        print(f"Changed IP address to {new_ip}")
        
        # Sleep for 5 seconds before changing again
        time.sleep(5)
    
    except KeyboardInterrupt:
        # Stop the script if Ctrl+C is pressed
        break
