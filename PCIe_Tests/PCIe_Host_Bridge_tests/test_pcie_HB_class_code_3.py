import os
import subprocess
import pytest

def get_host_bridge_bdf():
    result = subprocess.run(["lspci", "-nn"], capture_output=True, text=True)
    lines = result.stdout.splitlines()

    for line in lines:
        if "Host bridge" in line:
            host_bridge_bdf = line.split()[0]
            return host_bridge_bdf
    raise Exception("No PCIe Host Bridge found.")

def test_pcie_class_code():
    print("Fetching Host Bridge BDF...")
    bdf = get_host_bridge_bdf()
    print(f"Host Bridge BDF: {bdf}")

    class_path = f"/sys/bus/pci/devices/0000:{bdf}/class"
    print(f"Checking class code at {class_path}")
    
    with open(class_path, 'r') as f:
        class_code = f.read().strip()
        
    print(f"PCIe class code: {class_code}")
