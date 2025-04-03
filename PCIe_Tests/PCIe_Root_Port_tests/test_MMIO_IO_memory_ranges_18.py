import subprocess
import pytest

def get_lspci_output(bdf):
    """Get detailed lspci output for a given BDF."""
    try:
        result = subprocess.run(
            ["lspci", "-vvv", "-s", bdf], capture_output=True, text=True, check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running lspci for {bdf}: {e}")
        return None

def extract_mmio_io_ranges(lspci_output):
    """Extract MMIO and I/O ranges from the lspci -vvv output."""
    mmio_ranges = []
    io_ranges = []
    memory_behind_bridge = []
    io_behind_bridge = []
    
    for line in lspci_output.splitlines():
        # Extract MMIO ranges (lines containing 'Memory at')
        if 'Memory at' in line:
            mmio_ranges.append(line.strip())
        # Extract I/O ranges (lines containing 'I/O at' or 'I/O behind bridge')
        elif 'I/O at' in line:
            io_ranges.append(line.strip())
        # Extract Memory behind bridge
        elif 'Memory behind bridge' in line:
            memory_behind_bridge.append(line.strip())
        # Extract I/O behind bridge
        elif 'I/O behind bridge' in line:
            io_behind_bridge.append(line.strip())

    return mmio_ranges, io_ranges, memory_behind_bridge, io_behind_bridge

def test_pci_mmio_io_ranges():
    bdf = "00:01.0"  # Example BDF for the root port
    print(f"Checking MMIO and I/O ranges for PCI device {bdf}...")

    # Step 1: Get the detailed lspci output for the root port
    lspci_output = get_lspci_output(bdf)
    
    # Step 2: If no output, the device might not exist
    assert lspci_output is not None, f"Device {bdf} not found in lspci output"

    # Step 3: Extract MMIO and IO ranges
    mmio_ranges, io_ranges, memory_behind_bridge, io_behind_bridge = extract_mmio_io_ranges(lspci_output)

    # Print out extracted ranges for debugging
    print(f"MMIO Ranges for device {bdf}:")
    for range in mmio_ranges:
        print(range)

    print(f"I/O Ranges for device {bdf}:")
    for range in io_ranges:
        print(range)

    print(f"Memory behind bridge for device {bdf}:")
    for range in memory_behind_bridge:
        print(range)

    print(f"I/O behind bridge for device {bdf}:")
    for range in io_behind_bridge:
        print(range)


if __name__ == "__main__":
    pytest.main()
