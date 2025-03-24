import pytest

MMC_DEV_PATH = "/sys/class/mmc_host/mmc0/mmc0:4567/block/mmcblk0/dev"

def test_mmc_device_numbers():
    try:
        with open(MMC_DEV_PATH, "r") as f:
            dev_numbers = f.read().strip()
            print(f"MMC Device Numbers: {dev_numbers} (Major:Minor)")
        assert ":" in dev_numbers, "Invalid format for device numbers"
    except Exception as e:
        pytest.fail(f"Error reading MMC device numbers: {e}")
