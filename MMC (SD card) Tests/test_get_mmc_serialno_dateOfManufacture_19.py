import os
import pytest

MMC_PATH = "/sys/class/mmc_host/mmc0/mmc0:4567/"

def read_attr(attribute):
    path = os.path.join(MMC_PATH, attribute)
    try:
        with open(path, "r") as f:
            value = f.read().strip()
        print(f"{attribute}: {value}")
        return value
    except Exception as e:
        print(f"Failed to read {attribute}: {e}")
        return None

def test_serial_number_and_date():
    print("\nChecking MMC Serial Number and Manufacture Date...")

    serial_number = read_attr("serial")
    manufacture_date = read_attr("date")

    assert serial_number, "Serial number is missing!"
    assert manufacture_date, "Manufacture date is missing!"

    print("\nVerification Complete.")
    print(f"  - Serial Number: {serial_number}")
    print(f"  - Manufacture Date: {manufacture_date}")

    assert serial_number.startswith("0x"), "Serial number format may be incorrect!"
    assert "/" in manufacture_date, "Manufacture date format may be incorrect!"

