import os

device_bdf = "0000:00:01.0"
device_path = f"/sys/bus/pci/devices/{device_bdf}"

def test_root_port_subsystem_ids():
    try:
        # Retrieve Subsystem Vendor ID
        subsystem_vendor_path = os.path.join(device_path, "subsystem_vendor")
        with open(subsystem_vendor_path, "r") as f:
            subsystem_vendor_id = f.read().strip()
            print(f"Root Port Subsystem Vendor ID: {subsystem_vendor_id}")

        # Retrieve Subsystem Device ID
        subsystem_device_path = os.path.join(device_path, "subsystem_device")
        with open(subsystem_device_path, "r") as f:
            subsystem_device_id = f.read().strip()
            print(f"Root Port Subsystem Device ID: {subsystem_device_id}")

    except Exception as e:
        print(f"Error: {str(e)}")

