import os

device_bdf = "0000:00:01.0"
device_path = f"/sys/bus/pci/devices/{device_bdf}"

def test_root_port_vendor_device_ids():
    try:
        # Retrieve Vendor ID
        vendor_path = os.path.join(device_path, "vendor")
        with open(vendor_path, "r") as f:
            vendor_id = f.read().strip()
            print(f"Root Port Vendor ID: {vendor_id}")

        # Retrieve Device ID
        device_path_file = os.path.join(device_path, "device")
        with open(device_path_file, "r") as f:
            device_id = f.read().strip()
            print(f"Root Port Device ID: {device_id}")

    except Exception as e:
        print(f"Error: {str(e)}")

