import os

# Define the BDF of the device you're testing
device_bdf = "0000:00:00.0"
device_path = f"/sys/bus/pci/devices/{device_bdf}"

def test_pcie_irq():
    try:
        irq_path = os.path.join(device_path, "irq")
        with open(irq_path, "r") as f:
            irq = int(f.read().strip())
            print(f"irq: {irq}")
            if irq == 0:
                print("irq is 0, indicating no interrupt assigned.")
            else:
                print("irq is non-zero, indicating an interrupt is assigned.")
    except Exception as e:
        print(f"Error: {str(e)}")

