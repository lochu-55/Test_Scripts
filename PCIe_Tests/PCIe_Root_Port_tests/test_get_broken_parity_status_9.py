import os

device_bdf = "0000:00:01.0"
device_path = f"/sys/bus/pci/devices/{device_bdf}"

def test_root_port_broken_parity_status():
    try:
        broken_parity_status_path = os.path.join(device_path, "broken_parity_status")
        with open(broken_parity_status_path, "r") as f:
            broken_parity_status = f.read().strip()
            print(f"Root Port Broken Parity Status: {broken_parity_status}")
            if broken_parity_status not in ['0', '1']:
                raise Exception(f"Expected broken_parity_status to be 0 or 1, found {broken_parity_status}.")

    except Exception as e:
        print(f"Error: {str(e)}")

