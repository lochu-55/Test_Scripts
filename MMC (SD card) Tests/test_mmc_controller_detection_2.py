import os
import subprocess
import pytest

def run_command(cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return e.stdout.strip() + e.stderr.strip()

def test_mmc_host_exists():
    try:
        output = run_command("ls /sys/class/mmc_host/")
        print(f"MMC Host Output: {output}")
        assert "mmc0" in output, "No MMC host found"
    except Exception as e:
        pytest.fail(f"Error detecting MMC host: {e}")



