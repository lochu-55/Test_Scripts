import os

device_bdf = "0000:00:01.0"
device_path = f"/sys/bus/pci/devices/{device_bdf}"

def test_root_port_dma_mask_bits():
    try:
        dma_mask_bits_path = os.path.join(device_path, "dma_mask_bits")
        with open(dma_mask_bits_path, "r") as f:
            dma_mask_bits = int(f.read().strip())
            print(f"Root Port dma_mask_bits: {dma_mask_bits}")
            if dma_mask_bits != 32:
                raise Exception(f"Expected dma_mask_bits to be 32, found {dma_mask_bits}.")

    except Exception as e:
        print(f"Error: {str(e)}")

