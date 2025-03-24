import pytest

EXT_RANGE_PATH = "/sys/class/mmc_host/mmc0/mmc0:4567/block/mmcblk0/ext_range"

def test_ext_range():
    try:
        with open(EXT_RANGE_PATH, "r") as f:
            value = int(f.read().strip())
        print(f"ext_range: {value} - Represents the extended range for block allocation.")
        assert value >= 0  # Ensuring the value is non-negative
    except FileNotFoundError:
        print("Error: ext_range file not found.")
        raise
    except ValueError:
        print("Error: Invalid value in ext_range file.")
        raise

if __name__ == "__main__":
    pytest.main(["-s", "test_ext_range.py"])
