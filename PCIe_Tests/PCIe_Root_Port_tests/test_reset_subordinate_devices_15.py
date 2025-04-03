import subprocess
import os

device_bdf = "0000:00:01.0"
device_path = f"/sys/bus/pci/devices/{device_bdf}"

def test_trigger_subordinate_reset():
    try:
        reset_subordinate_path = os.path.join(device_path, "reset_subordinate")
        
        # Use echo and sudo tee to write to the file
        command = f"echo 1 | sudo tee {reset_subordinate_path}"
        
        # Execute the command
        subprocess.run(command, shell=True, check=True)
        print("Subordinate reset triggered successfully.")

    except Exception as e:
        print(f"Error: {str(e)}")


