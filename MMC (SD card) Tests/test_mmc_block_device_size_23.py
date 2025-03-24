import os
import pytest

MMC_SIZE_PATH = "/sys/class/mmc_host/mmc0/mmc0:4567/block/mmcblk0/size"

def test_mmc_size():
    try:
        with open(MMC_SIZE_PATH, "r") as f:
            size = int(f.read().strip())
        assert size > 0, f"MMC size is invalid: {size}"
        print(f"MMC size is valid: {size} blocks")
    except FileNotFoundError:
        print("Error: MMC size file not found.")
        raise
    except ValueError:
        print("Error: Invalid value in MMC size file.")
        raise

if __name__ == "__main__":
    pytest.main(["-v", "test_mmc_size.py"])
