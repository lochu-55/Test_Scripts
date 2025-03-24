import pytest
import subprocess


def test_sd_card_storage_size():
    print("\nChecking SD Card Total Storage Size...\n")

    try:
        # Read total storage size in blocks
        total_size_blocks = subprocess.run(
            "cat /sys/block/mmcblk0/size",
            shell=True, capture_output=True, text=True
        ).stdout.strip()

        print(f"Total Storage Size: {total_size_blocks} blocks")

    except Exception as e:
        print(f"Error fetching storage size: {e}")

if __name__ == "__main__":
    test_sd_card_storage_size()
