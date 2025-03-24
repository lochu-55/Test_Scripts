import os
import pytest

MMC_RO_PATH = "/sys/class/mmc_host/mmc0/mmc0:4567/block/mmcblk0/ro"

def test_mmc_read_only():
    try:
        with open(MMC_RO_PATH, "r") as f:
            ro_status = f.read().strip()
        assert ro_status == "0", "MMC is in read-only mode"
        print("MMC is not read-only.")
    except FileNotFoundError:
        print("Error: Read-only status file not found.")
        raise
    except AssertionError as e:
        print(f"Error: {e}")
        raise

if __name__ == "__main__":
    pytest.main(["-v", "test_mmc_read_only.py"])
