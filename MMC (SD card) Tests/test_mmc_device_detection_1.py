import os
import subprocess
import pytest

def run_command(cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return e.stdout.strip() + e.stderr.strip()



def test_mmc_device_in_dev():
    try:
        output = run_command("ls /dev | grep mmc")
        print(f"MMC Devices in /dev: {output}")
        assert "mmcblk" in output, "No MMC device found in /dev"
    except Exception as e:
        pytest.fail(f"Error detecting MMC device: {e}")
