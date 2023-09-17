import subprocess
import time
import random

# Network interface name (e.g., eth0, wlan0)
interface_name = "eth0"

while True:
    try:
        # Generate a random IP address (for demonstration purposes)
        new_ip = "192.168." + str(random.randint(0, 255)) + "." + str(random.randint(0, 255))
        
        # Change the IP address using ifconfig (you may need to adjust this for your Linux distribution)
        subprocess.run(["sudo", "ifconfig", interface_name, new_ip])
        
        print(f"Changed IP address to {new_ip}")
        
        # Sleep for 5 seconds before changing again
        time.sleep(5)
    
    except KeyboardInterrupt:
        # Stop the script if Ctrl+C is pressed
        break
