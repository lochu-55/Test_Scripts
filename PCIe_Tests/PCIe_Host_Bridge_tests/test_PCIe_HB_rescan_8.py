import subprocess
import time

def test_rescan():
    try:
        # Define the PCIe device BDF and rescan path
        bdf = '0000:00:00.0'
        rescan_path = f"/sys/bus/pci/devices/{bdf}/rescan"
        
        # Trigger rescan
        print(f"Triggering rescan for device {bdf}...")
        result = subprocess.run(
            ['echo', '1', '|', 'sudo', 'tee', rescan_path],
            capture_output=True, text=True, shell=True
        )
        
        # Check if the rescan command was successful
        if result.returncode == 0:
            print(f"Rescan triggered successfully for device {bdf}")
        else:
            print(f"Failed to trigger rescan for device {bdf}")
            print("Error:", result.stderr)
            return
        
        # Optionally, wait for a few seconds to allow the system to process the rescan
        time.sleep(2)
        
        # Verify if the PCI device is still present after rescan
        result = subprocess.run(
            ['lspci', '|', 'grep', bdf],
            capture_output=True, text=True, shell=True
        )
        
        if result.returncode == 0:
            print(f"PCI device {bdf} found after rescan")
        else:
            print(f"PCI device {bdf} not found after rescan")
    
    except Exception as e:
        print(f"Error during rescan test: {e}")
        raise


