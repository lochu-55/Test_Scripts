import subprocess

device_bdf = "0000:00:01.0"
rescan_path = f"/sys/bus/pci/devices/{device_bdf}/rescan"

def test_rescan_pci_bus():
    try:
        print("Triggering PCI rescan...")
        subprocess.run(["echo", "1"], check=True)
        subprocess.run(["sudo", "tee", rescan_path], input=b"1\n", check=True)
        print("PCI rescan triggered successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")


