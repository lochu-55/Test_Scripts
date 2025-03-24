import os
import pytest

MMC_FORCE_RO_PATH = "/sys/class/mmc_host/mmc0/mmc0:4567/block/mmcblk0/force_ro"

def test_mmc_force_ro():
    try:
        with open(MMC_FORCE_RO_PATH, "r") as f:
            force_ro_status = f.read().strip()
        assert force_ro_status == "0", "MMC is forcibly read-only"
        print("MMC is not forcibly read-only.")
    except FileNotFoundError:
        print("Error: Force read-only file not found.")
        raise

if __name__ == "__main__":
    pytest.main(["-v", "test_mmc_force_ro.py"])
