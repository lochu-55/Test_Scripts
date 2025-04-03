import os

# Define the BDF (Bus/Device/Function) of the device you're testing (Root Port in this case)
device_bdf = "0000:00:01.0"
device_path = f"/sys/bus/pci/devices/{device_bdf}"

def test_root_port_secondary_bus_number():
    try:
        secondary_bus_number_path = os.path.join(device_path, "secondary_bus_number")
        with open(secondary_bus_number_path, "r") as f:
            secondary_bus_number = f.read().strip()
            print(f"Root Port Secondary Bus Number: {secondary_bus_number}")
            if not secondary_bus_number.isdigit():
                raise Exception(f"Expected secondary_bus_number to be a number, found {secondary_bus_number}.")

    except Exception as e:
        print(f"Error: {str(e)}")

def test_root_port_subordinate_bus_number():
    try:
        subordinate_bus_number_path = os.path.join(device_path, "subordinate_bus_number")
        with open(subordinate_bus_number_path, "r") as f:
            subordinate_bus_number = f.read().strip()
            print(f"Root Port Subordinate Bus Number: {subordinate_bus_number}")
            if not subordinate_bus_number.isdigit():
                raise Exception(f"Expected subordinate_bus_number to be a number, found {subordinate_bus_number}")

    except Exception as e:
        print(f"Error: {str(e)}")

