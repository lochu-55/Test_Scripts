import subprocess
import pytest

def run_command(cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return e.stdout.strip() + e.stderr.strip()

def test_mmc_card_detected():
    try:
        # Check if any MMC card is listed
        output = run_command("ls /sys/class/mmc_host/mmc0/")
        detected = any("mmc0:" in line for line in output.split("\n"))
        
        # Fetch the actual MMC identifier (e.g., mmc0:4567)
        mmc_identifiers = run_command("ls /sys/class/mmc_host/mmc0/")
        mmc_id = [line for line in mmc_identifiers.split("\n") if line.startswith("mmc0:")]
        
        print(f"MMC Card Detection Output: {detected}")
        print(f"MMC Card Identifier(s): {mmc_id}")
        
        assert detected, "No MMC/SD card detected"
        assert mmc_id, "No MMC identifier found"
    
    except Exception as e:
        pytest.fail(f"Error detecting MMC card: {e}")
