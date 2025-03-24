import pytest

MMC_SYSFS_RANGE = "/sys/class/mmc_host/mmc0/mmc0:4567/block/mmcblk0/range"


def test_mmc_supported_partitions():
    try:
        print(f"Opening {MMC_SYSFS_RANGE} to read partition support info...")
        with open(MMC_SYSFS_RANGE, "r") as f:
            max_partitions = int(f.read().strip())

        print(f"SUCCESS: MMC device supports up to {max_partitions} partitions.")
    except FileNotFoundError:
        print(f"ERROR: File not found - {MMC_SYSFS_RANGE}")
        pytest.fail(f"Range file not found: {MMC_SYSFS_RANGE}")
    except PermissionError:
        print(f"ERROR: Permission denied while accessing {MMC_SYSFS_RANGE}.")
        pytest.fail(f"Permission denied: {MMC_SYSFS_RANGE}. Try running as root.")
    except ValueError:
        print(f"ERROR: Invalid content found in {MMC_SYSFS_RANGE}.")
        pytest.fail(f"Invalid content in range file: {MMC_SYSFS_RANGE}")
