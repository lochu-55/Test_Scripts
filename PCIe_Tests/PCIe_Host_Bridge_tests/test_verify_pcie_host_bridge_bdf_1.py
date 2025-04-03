import os
import subprocess
import pytest

def test_get_host_bridge_bdf():
    result = subprocess.run(["lspci", "-nn"], capture_output=True, text=True)
    lines = result.stdout.splitlines()

    for line in lines:
        if "Host bridge" in line:
            host_bridge_bdf = line.split()[0]
            print(f"Found PCIe Host Bridge with BDF value : {host_bridge_bdf}")
            assert host_bridge_bdf, "Host Bridge BDF not found"

