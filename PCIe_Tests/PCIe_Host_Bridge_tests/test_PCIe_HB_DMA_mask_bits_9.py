import os

# Define the BDF of the device you're testing
device_bdf = "0000:00:00.0"
device_path = f"/sys/bus/pci/devices/{device_bdf}"

def test_pcie_dma_mask_bits():
    try:
        dma_mask_bits_path = os.path.join(device_path, "dma_mask_bits")
        with open(dma_mask_bits_path, "r") as f:
            dma_mask_bits = int(f.read().strip())
            print(f"dma_mask_bits: {dma_mask_bits}")
            if dma_mask_bits != 32:
                raise Exception(f"Expected dma_mask_bits to be 32, found {dma_mask_bits}.")
            else:
                print("dma_mask_bits verification passed.")
    except Exception as e:
        print(f"Error: {str(e)}")

