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

def test_broken_parity_status():
    try:
        bdf = get_pcie_device_bdf()
        file_path = f"/sys/bus/pci/devices/0000:{bdf}/broken_parity_status"
        with open(file_path, 'r') as f:
            status = f.read().strip()
            print(f"Broken Parity Status: {status}")
    except Exception as e:
        print(f"Error in test_broken_parity_status: {e}")
        raise
