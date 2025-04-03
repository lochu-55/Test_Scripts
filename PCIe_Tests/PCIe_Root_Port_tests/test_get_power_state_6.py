import os

device_bdf = "0000:00:01.0"
device_path = f"/sys/bus/pci/devices/{device_bdf}"

def test_root_port_power_state():
    try:
        # Retrieve Power State
        power_state_path = os.path.join(device_path, "power_state")
        with open(power_state_path, "r") as f:
            power_state = f.read().strip()
            print(f"Root Port Power State: {power_state}")

    except Exception as e:
        print(f"Error: {str(e)}")

