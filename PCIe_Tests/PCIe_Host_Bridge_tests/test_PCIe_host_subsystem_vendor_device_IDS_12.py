import os

# Define the BDF (Bus/Device/Function) of the device you're testing
device_bdf = "0000:00:00.0"
device_path = f"/sys/bus/pci/devices/{device_bdf}"

def test_pcie_ids():
    try:
        # Retrieve Vendor ID
        vendor_path = os.path.join(device_path, "vendor")
        with open(vendor_path, "r") as f:
            vendor_id = f.read().strip()
            print(f"Vendor ID: {vendor_id}")

        # Retrieve Device ID
        device_path_file = os.path.join(device_path, "device")
        with open(device_path_file, "r") as f:
            device_id = f.read().strip()
            print(f"Device ID: {device_id}")

        # Retrieve Subsystem Vendor ID
        subsystem_vendor_path = os.path.join(device_path, "subsystem_vendor")
        with open(subsystem_vendor_path, "r") as f:
            subsystem_vendor_id = f.read().strip()
            print(f"Subsystem Vendor ID: {subsystem_vendor_id}")

        # Retrieve Subsystem Device ID
        subsystem_device_path = os.path.join(device_path, "subsystem_device")
        with open(subsystem_device_path, "r") as f:
            subsystem_device_id = f.read().strip()
            print(f"Subsystem Device ID: {subsystem_device_id}")

    except Exception as e:
        print(f"Error: {str(e)}")

