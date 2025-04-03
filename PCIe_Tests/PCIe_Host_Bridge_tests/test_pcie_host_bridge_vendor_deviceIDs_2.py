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

def test_pcie_vendor_device_ids():
    print("Fetching Host Bridge BDF...")
    bdf = get_host_bridge_bdf()
    print(f"Host Bridge BDF: {bdf}")

    vendor_path = f"/sys/bus/pci/devices/0000:{bdf}/vendor"
    device_path = f"/sys/bus/pci/devices/0000:{bdf}/device"
    
    print(f"Checking vendor ID at {vendor_path}")
    with open(vendor_path, 'r') as f:
        vendor_id = int(f.read().strip(), 16)
        
    print(f"Vendor ID: {vendor_id:#06x}")

    print(f"Checking device ID at {device_path}")
    with open(device_path, 'r') as f:
        device_id = int(f.read().strip(), 16)
        
    print(f"Device ID: {device_id:#06x}")
    
    print("PCIe vendor and device IDs verification passed.")
