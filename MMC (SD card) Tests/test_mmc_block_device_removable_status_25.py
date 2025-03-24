import os
import pytest

MMC_REMOVABLE_PATH = "/sys/class/mmc_host/mmc0/mmc0:4567/block/mmcblk0/removable"

def test_mmc_removable():
    try:
        with open(MMC_REMOVABLE_PATH, "r") as f:
            removable_status = f.read().strip()
        
        assert removable_status in ["0", "1"], "Invalid removable status"

        if removable_status == "0":
            print("MMC is **not** removable (fixed storage).")
        else:
            print("MMC **is** removable (removable storage).")

    except FileNotFoundError:
        print("Error: Removable status file not found.")
        raise

if __name__ == "__main__":
    pytest.main(["-v", "test_mmc_removable.py"])
