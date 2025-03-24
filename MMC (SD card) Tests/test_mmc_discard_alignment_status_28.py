import pytest

MMC_DISCARD_PATH = "/sys/class/mmc_host/mmc0/mmc0:4567/block/mmcblk0/discard_alignment"

def test_mmc_discard_alignment():
    try:
        with open(MMC_DISCARD_PATH, "r") as f:
            discard = int(f.read().strip())

        assert discard >= 0

        print(f"MMC discard alignment: {discard}")
        if discard == 0:
            print("Discard (TRIM) commands can be issued without alignment restrictions.")
        else:
            print("Discard operations should be aligned to that many bytes for efficiency.")

    except FileNotFoundError:
        print("Error: Discard alignment file not found.")
        raise
    except ValueError:
        print("Error: Invalid value in discard alignment file.")
        raise

if __name__ == "__main__":
    pytest.main(["-v", "test28_mmc_discard_alignment_status.py"])
