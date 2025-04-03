import os

# Define the BDF of the device you're testing
device_bdf = "0000:00:00.0"
device_path = f"/sys/bus/pci/devices/{device_bdf}"

def test_pcie_enable():
    try:
        enable_path = os.path.join(device_path, "enable")
        with open(enable_path, "r") as f:
            enable = int(f.read().strip())
            print(f"enable: {enable}")
            if enable == 0:
                print("Device is disabled...")
            else:
                print("Device is enabled...")
    except Exception as e:
        print(f"Error: {str(e)}")

