import subprocess
import pytest
import re

def run_command(cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return e.stdout.strip() + e.stderr.strip()

def test_mmc_read_time():
    output = run_command("sudo dd if=/dev/mmcblk0 of=/dev/null bs=1M count=100 2>&1 | tail -n 1")
    print(f"MMC Read Time Output:\n{output}")

    match = re.search(r"(\d+\.\d+)\s+s", output)
    assert match, "Failed to extract read time"

    time_taken = float(match.group(1))
    print(f"MMC Read Time: {time_taken} s")
    assert time_taken > 0, "Read time should be greater than 0 seconds"
