import pytest

INFLIGHT_PATH = "/sys/class/mmc_host/mmc0/mmc0:4567/block/mmcblk0/inflight"

def test_inflight():
    try:
        with open(INFLIGHT_PATH, "r") as f:
            reads, writes = map(int, f.read().strip().split())
        print(f"inflight: {reads} read requests, {writes} write requests are currently pending.")
        assert reads >= 0 and writes >= 0
    except FileNotFoundError:
        print("Error: inflight file not found.")
        raise
    except ValueError:
        print("Error: Invalid value in inflight file.")
        raise

if __name__ == "__main__":
    pytest.main(["-s", "test_inflight.py"])
