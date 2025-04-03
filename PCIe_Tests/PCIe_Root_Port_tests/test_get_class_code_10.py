import os

device_bdf = "0000:00:01.0"
device_path = f"/sys/bus/pci/devices/{device_bdf}"

def test_root_port_class_code():
    try:
        class_code_path = os.path.join(device_path, "class")
        with open(class_code_path, "r") as f:
            class_code = f.read().strip()
            print(f"Root Port Class Code: {class_code}")
            if not class_code.startswith('0x'):
                raise Exception(f"Expected class code to be in hexadecimal format, found {class_code}.")

    except Exception as e:
        print(f"Error: {str(e)}")

