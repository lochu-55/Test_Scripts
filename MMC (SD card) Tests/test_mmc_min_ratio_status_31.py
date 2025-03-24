import pytest

MIN_RATIO_PATH = "/sys/class/mmc_host/mmc0/mmc0:4567/block/mmcblk0/bdi/min_ratio"
MIN_RATIO_FINE_PATH = "/sys/class/mmc_host/mmc0/mmc0:4567/block/mmcblk0/bdi/min_ratio_fine"

def test_min_ratio():
    try:
        with open(MIN_RATIO_PATH, "r") as f:
            min_ratio = int(f.read().strip())
        print(f"min_ratio: {min_ratio}% - Minimum percentage of memory kept free.")
        assert min_ratio >= 0
    except Exception as e:
        print(f"Error reading min_ratio: {e}")
        raise

def test_min_ratio_fine():
    try:
        with open(MIN_RATIO_FINE_PATH, "r") as f:
            min_ratio_fine = int(f.read().strip())
        print(f"min_ratio_fine: {min_ratio_fine} - Finer granularity for min_ratio.")
        assert min_ratio_fine >= 0
    except Exception as e:
        print(f"Error reading min_ratio_fine: {e}")
        raise

if __name__ == "__main__":
    pytest.main(["-v", "test_min_ratio.py"])
