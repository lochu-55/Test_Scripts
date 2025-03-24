import os
import pytest

MMC_PATH = "/sys/class/mmc_host/mmc0/mmc0:4567/"

def read_attr(attribute):
    path = os.path.join(MMC_PATH, attribute)
    try:
        with open(path, "r") as f:
            value = int(f.read().strip())  # Convert to integer
        print(f"{attribute}: {value} bytes")
        return value
    except Exception as e:
        print(f"Failed to read {attribute}: {e}")
        return None

def test_erase_sizes():
    print("\nChecking MMC erase properties...")

    # Read values
    erase_size = read_attr("erase_size")
    preferred_erase_size = read_attr("preferred_erase_size")

    # Ensure values are valid
    assert erase_size and preferred_erase_size, "Erase size attributes are missing!"
    
    print("\nDifference between erase_size and preferred_erase_size:")
    print(f"  - erase_size: Minimum bytes that can be erased at once.")
    print(f"  - preferred_erase_size: Recommended erase size for better performance.")

    # Comparison
    if preferred_erase_size > erase_size:
        print(f"\nPreferred erase size ({preferred_erase_size} bytes) is larger than erase size ({erase_size} bytes).")
    else:
        print(f"\nWARNING: Preferred erase size ({preferred_erase_size} bytes) is small!")

    # Check if preferred_erase_size is a multiple of erase_size
    if preferred_erase_size % erase_size == 0:
        print("Preferred erase size is a multiple of erase size.")
    else:
        print("WARNING: Preferred erase size is NOT a multiple of erase size!")

    # Final assertions
    assert preferred_erase_size >= erase_size, "Preferred erase size should be larger than erase size!"
    assert preferred_erase_size % erase_size == 0, "Preferred erase size should be a multiple of erase size!"

