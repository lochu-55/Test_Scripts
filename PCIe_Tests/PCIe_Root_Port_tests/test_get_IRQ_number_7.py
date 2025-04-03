import os

# Define the BDF (Bus/Device/Function) of the device you're testing (Root Port in this case)
device_bdf = "0000:00:01.0"
device_path = f"/sys/bus/pci/devices/{device_bdf}"

def test_root_port_irq():
    try:
        irq_path = os.path.join(device_path, "irq")
        with open(irq_path, "r") as f:
            irq = f.read().strip()
            print(f"Root Port IRQ: {irq}")
            if not irq.isdigit():
                raise Exception(f"Expected IRQ to be a number, but found {irq}.")

    except Exception as e:
        print(f"Error: {str(e)}")

