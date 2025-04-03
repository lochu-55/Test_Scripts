import os

device_bdf = "0000:00:01.0"
device_path = f"/sys/bus/pci/devices/{device_bdf}"

def test_root_port_enable():
    try:
        enable_path = os.path.join(device_path, "enable")
        with open(enable_path, "r") as f:
            enable = f.read().strip()
            print(f"Root Port Enable bit: {enable}")
            if enable == 0:
                print("Root port is disabled")
            else :
                print("Root port is enabled")
            if enable not in ['0', '1']:
                raise Exception(f"Expected enable to be 0 or 1, found {enable}.")

    except Exception as e:
        print(f"Error: {str(e)}")

