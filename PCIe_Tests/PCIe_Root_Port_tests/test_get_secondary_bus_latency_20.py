import subprocess
import pytest

def get_lspci_output(bdf):
    try:
        result = subprocess.run(
            ["lspci", "-vvv", "-s", bdf], capture_output=True, text=True, check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running lspci for {bdf}: {e}")

def extract_secondary_latency(lspci_output):
    for line in lspci_output.splitlines():
        if 'sec-latency=' in line:
            # Extract the latency value
            latency_value = line.split('sec-latency=')[1].split()[0]
            return int(latency_value)

def test_secondary_latency():
    bdf = "00:01.0"  # Example BDF for the PCI bridge device
    print(f"Checking secondary latency for PCI device {bdf}...")

    lspci_output = get_lspci_output(bdf)

    sec_latency = extract_secondary_latency(lspci_output)

    print(f"Secondary latency for device {bdf}: {sec_latency}")


