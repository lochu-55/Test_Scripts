import pytest
import subprocess



def test_sd_card_info():
    print("\nChecking SD Card Information...\n")

    try:
        # Retrieve manufacturer ID
        manfid = subprocess.run(
            "cat /sys/class/mmc_host/mmc0/mmc0:*/manfid",
            shell=True, capture_output=True, text=True
        ).stdout.strip()

        # Retrieve OEM ID
        oemid = subprocess.run(
            "cat /sys/class/mmc_host/mmc0/mmc0:*/oemid",
            shell=True, capture_output=True, text=True
        ).stdout.strip()


        print(f"Manufacturer ID: {manfid}")
        print(f"OEM ID: {oemid}")

    except Exception as e:
        print(f"Error fetching SD card information: {e}")

if __name__ == "__main__":
    test_sd_card_info()
