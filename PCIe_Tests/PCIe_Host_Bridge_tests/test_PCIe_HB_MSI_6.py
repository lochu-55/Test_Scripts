import subprocess
import os

def get_pcie_device_bdf():
    try:
        result = subprocess.run(["lspci", "-nn"], capture_output=True, text=True)
        lines = result.stdout.splitlines()
        for line in lines:
            if "Host bridge" in line:
                host_bridge_bdf = line.split()[0]
                print(f"Found PCIe Host Bridge with BDF value : {host_bridge_bdf}")
                return host_bridge_bdf
        raise Exception("No PCIe Host Bridge found.")
    except Exception as e:
        print(f"Error while fetching BDF: {e}")
        raise



def test_msi_bus():
    try:
        bdf = get_pcie_device_bdf()
        file_path = f"/sys/bus/pci/devices/0000:{bdf}/msi_bus"
        with open(file_path, 'r') as f:
            msi_support = f.read().strip()
            print(f"MSI Bus Support: {msi_support}")
            if msi_support == '1':
                print("MSI is supported.")
            else:
                print("MSI is not supported.")
    except Exception as e:
        print(f"Error in test_msi_bus: {e}")
        raise
