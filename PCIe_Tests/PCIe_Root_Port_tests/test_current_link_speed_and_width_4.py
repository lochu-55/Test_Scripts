import os

device_bdf = "0000:00:01.0"
device_path = f"/sys/bus/pci/devices/{device_bdf}"

def test_root_port_link_speed_width():
    try:
        # Retrieve Current Link Speed
        link_speed_path = os.path.join(device_path, "current_link_speed")
        with open(link_speed_path, "r") as f:
            link_speed = f.read().strip()
            print(f"Root Port Current Link Speed: {link_speed}")

        # Retrieve Current Link Width
        link_width_path = os.path.join(device_path, "current_link_width")
        with open(link_width_path, "r") as f:
            link_width = f.read().strip()
            print(f"Root Port Current Link Width: {link_width}")

    except Exception as e:
        print(f"Error: {str(e)}")

