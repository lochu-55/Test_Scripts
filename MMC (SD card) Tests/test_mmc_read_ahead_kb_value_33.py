import pytest

READ_AHEAD_PATH = "/sys/class/mmc_host/mmc0/mmc0:4567/block/mmcblk0/bdi/read_ahead_kb"

def test_read_ahead():
    try:
        with open(READ_AHEAD_PATH, "r") as f:
            read_ahead = int(f.read().strip())
        print(f"read_ahead_kb: {read_ahead} KB - Amount of data read in advance for sequential access.")
        assert read_ahead >= 0
    except Exception as e:
        print(f"Error reading read_ahead_kb: {e}")
        raise

if __name__ == "__main__":
    pytest.main(["-v", "test_read_ahead.py"])

