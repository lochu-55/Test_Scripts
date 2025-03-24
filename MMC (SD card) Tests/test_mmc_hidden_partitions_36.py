import pytest

HIDDEN_PATH = "/sys/class/mmc_host/mmc0/mmc0:4567/block/mmcblk0/hidden"

def test_hidden():
    try:
        with open(HIDDEN_PATH, "r") as f:
            value = int(f.read().strip())
        if value == 0:
            print("hidden: 0 - No hidden partitions.")
        else:
            print(f"hidden: {value} - There are hidden partitions.")
        assert value in [0, 1]
    except FileNotFoundError:
        print("Error: hidden file not found.")
        raise
    except ValueError:
        print("Error: Invalid value in hidden file.")
        raise

if __name__ == "__main__":
    pytest.main(["-s", "test_hidden.py"])
