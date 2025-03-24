import subprocess
import pytest
import re

def run_command(cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
        return result.stdout.strip() + "\n" + result.stderr.strip()
    except subprocess.CalledProcessError as e:
        return e.stdout.strip() + "\n" + e.stderr.strip()

def parse_speed(output):
    lines = output.split("\n")
    
    # Find the last line that contains a speed measurement
    for line in reversed(lines):
        match = re.search(r"(\d+(\.\d+)?)\s+(MB/s|KB/s|GB/s)", line)
        if match:
            return match.group(0)  # Return the matched speed value

    return None  # Return None if no speed is found

def test_mmc_read_speed():
    try:
        output = run_command("sudo dd if=/dev/mmcblk0 of=/dev/null bs=1M count=100 status=progress 2>&1")
        print(f"MMC Read Speed Output:\n{output}")

        speed = parse_speed(output)
        assert speed, "Failed to extract read speed"

        print(f"Final MMC Read Speed: {speed}")

    except Exception as e:
        pytest.fail(f"Error measuring MMC read speed: {e}")
