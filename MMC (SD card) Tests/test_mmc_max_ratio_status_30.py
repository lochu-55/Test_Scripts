import pytest

MAX_RATIO_PATH = "/sys/class/mmc_host/mmc0/mmc0:4567/block/mmcblk0/bdi/max_ratio"
MAX_RATIO_FINE_PATH = "/sys/class/mmc_host/mmc0/mmc0:4567/block/mmcblk0/bdi/max_ratio_fine"

def test_max_ratio():
    try:
        with open(MAX_RATIO_PATH, "r") as f:
            max_ratio = int(f.read().strip())
        print(f"max_ratio: {max_ratio}% - Maximum percentage of memory allowed for dirty pages.")
        assert max_ratio >= 0
    except Exception as e:
        print(f"Error reading max_ratio: {e}")
        raise

def test_max_ratio_fine():
    try:
        with open(MAX_RATIO_FINE_PATH, "r") as f:
            max_ratio_fine = int(f.read().strip())
        print(f"max_ratio_fine: {max_ratio_fine} - Finer granularity for max_ratio.")
        assert max_ratio_fine >= 0
    except Exception as e:
        print(f"Error reading max_ratio_fine: {e}")
        raise

if __name__ == "__main__":
    pytest.main(["-v", "test_max_ratio.py"])
