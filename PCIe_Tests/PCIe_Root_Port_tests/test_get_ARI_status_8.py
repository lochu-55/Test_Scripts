import os

device_bdf = "0000:00:01.0"
device_path = f"/sys/bus/pci/devices/{device_bdf}"

def test_root_port_ari_enabled():
    try:
        ari_enabled_path = os.path.join(device_path, "ari_enabled")
        with open(ari_enabled_path, "r") as f:
            ari_enabled = f.read().strip()
        
        print(f"Root Port ARI Enabled bit: {ari_enabled}")

        # Convert to integer before checking
        if ari_enabled == '0':
            print("ARI is disabled")
        elif ari_enabled == '1':
            print("ARI is enabled")
        else:
            raise Exception(f"Unexpected ARI Enabled value: {ari_enabled}")

    except Exception as e:
        print(f"Error: {str(e)}")

