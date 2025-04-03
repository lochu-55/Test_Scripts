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

def extract_kernel_driver(lspci_output):
    for line in lspci_output.splitlines():
        if 'Kernel driver in use' in line:
            # Extract the driver name
            driver = line.split(":")[-1].strip()
            return driver

def test_kernel_driver_for_pcieport():
    bdf = "00:01.0"  # Example BDF for the root port
    print(f"Checking kernel driver for PCI device {bdf}...")

    lspci_output = get_lspci_output(bdf)
    
    kernel_driver = extract_kernel_driver(lspci_output)

    # Print out extracted driver for debugging
    print(f"Kernel Driver for device {bdf}: {kernel_driver}")


if __name__ == "__main__":
    pytest.main()
