import os

device_bdf = "0000:00:01.0"
device_path = f"/sys/bus/pci/devices/{device_bdf}"

def test_root_port_msi_bus():
    try:
        msi_bus_path = os.path.join(device_path, "msi_bus")
        if os.path.exists(msi_bus_path):
            with open(msi_bus_path, "r") as f:
                msi_bus = f.read().strip()
            print(f"MSI Bus support: {msi_bus}")
        else:
            print("MSI Bus support is not available for this device.")
    
    except Exception as e:
        print(f"Error: {str(e)}")
