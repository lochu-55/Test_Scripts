import pytest

PARTSCAN_PATH = "/sys/class/mmc_host/mmc0/mmc0:4567/block/mmcblk0/partscan"

def test_partscan():
    try:
        with open(PARTSCAN_PATH, "r") as f:
            value = int(f.read().strip())
        if value == 1:
            print("partscan: 1 - Partition scanning is enabled.")
        else:
            print("partscan: 0 - Partition scanning is disabled.")
        assert value in [0, 1]
    except FileNotFoundError:
        print("Error: partscan file not found.")
        raise
    except ValueError:
        print("Error: Invalid value in partscan file.")
        raise

if __name__ == "__main__":
    pytest.main(["-s", "test_partscan.py"])
