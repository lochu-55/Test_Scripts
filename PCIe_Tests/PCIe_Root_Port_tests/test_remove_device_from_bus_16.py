import subprocess
import time

device_bdf = "00:01.0"  # PCI device BDF

def is_device_present(device_bdf):
    try:
        # Run lspci and capture its output
        result = subprocess.run(["lspci"], capture_output=True, text=True)
        lspci_output = result.stdout
        
        # Search for the device BDF in the lspci output
        for line in lspci_output.splitlines():
            if device_bdf in line:
                return True
        return False

    except Exception as e:
        print(f"Error checking device presence: {str(e)}")
        return False


def test_device_removal():
    try:
        #with open(f"/sys/bus/pci/devices/0000:{device_bdf}/remove", "w") as f:
            #f.write("1")
        print(f"PCI device {device_bdf} removal triggered.")
    except Exception as e:
        print(f"Error removing device: {str(e)}")
    
    # Wait a few seconds to allow the removal process to complete
    time.sleep(2)
    
    # Check if the device is still present after removal
    if is_device_present(device_bdf):
        print(f"Device {device_bdf} is still present on the bus after removal.")
    else:
        print(f"Device {device_bdf} is not present on the bus after removal attempt.")
