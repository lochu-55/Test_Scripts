import pytest

STRICT_LIMIT_PATH = "/sys/class/mmc_host/mmc0/mmc0:4567/block/mmcblk0/bdi/strict_limit"

def test_strict_limit():
    try:
        with open(STRICT_LIMIT_PATH, "r") as f:
            strict_limit = int(f.read().strip())
        print(f"strict_limit: {strict_limit} - Enforces strict limit on dirty memory usage.")
        assert strict_limit in [0, 1]
    except Exception as e:
        print(f"Error reading strict_limit: {e}")
        raise

if __name__ == "__main__":
    pytest.main(["-v", "test_strict_limit.py"])
