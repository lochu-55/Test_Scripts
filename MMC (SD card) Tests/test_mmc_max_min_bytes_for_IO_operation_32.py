import pytest

MAX_BYTES_PATH = "/sys/class/mmc_host/mmc0/mmc0:4567/block/mmcblk0/bdi/max_bytes"
MIN_BYTES_PATH = "/sys/class/mmc_host/mmc0/mmc0:4567/block/mmcblk0/bdi/min_bytes"

def test_max_bytes():
    try:
        with open(MAX_BYTES_PATH, "r") as f:
            max_bytes = int(f.read().strip())
        print(f"max_bytes: {max_bytes} - Maximum allowed I/O operation size.")
        assert max_bytes > 0
    except Exception as e:
        print(f"Error reading max_bytes: {e}")
        raise

def test_min_bytes():
    try:
        with open(MIN_BYTES_PATH, "r") as f:
            min_bytes = int(f.read().strip())
        print(f"min_bytes: {min_bytes} - Minimum cached bytes before a write is forced.")
        assert min_bytes >= 0
    except Exception as e:
        print(f"Error reading min_bytes: {e}")
        raise

if __name__ == "__main__":
    pytest.main(["-v", "test_bytes.py"])
