import subprocess

def test_get_root_port_bdf():
    try:
        # Run lspci to get all PCI devices
        result = subprocess.run(["lspci"], capture_output=True, text=True)
        lspci_output = result.stdout
        
        # Look for the Root Port specifically (not just PCI bridge)
        for line in lspci_output.splitlines():
            if "Root port" in line:
                # Extract the BDF from the first column
                bdf = line.split()[0]
                print(f"Root Port BDF: {bdf}")
        

    except Exception as e:
        print(f"Error extracting Root Port BDF: {str(e)}")

