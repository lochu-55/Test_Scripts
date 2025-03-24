import subprocess
import re
import pytest

DEVICE = "/dev/mmcblk0"  # Update if needed

def get_hdparm_output(device=DEVICE):
    try:
        result = subprocess.run(["sudo", "hdparm", "-tT", device], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"hdparm command failed: {e.stderr}"

def parse_buffered_read_speed(output):
    match = re.search(r"Timing buffered disk reads:\s+(\d+)\s+MB in\s+[\d.]+\s+seconds\s+=\s+([\d.]+)\s+MB/sec", output)
    return float(match.group(2)) if match else None


def test_sd_card_timing():
    print("\nRunning hdparm Test...")
    
    output = get_hdparm_output()
    print("\nHDParm Test Results:\n", output)

    buffered_read_speed = parse_buffered_read_speed(output)
    
    print("\nSD Card Timing Results:")
    if buffered_read_speed is not None:
        print(f"Buffered Disk Read Speed: {buffered_read_speed} MB/sec")
    else:
        print("Could not extract buffered read speed from hdparm output.")

if __name__ == "__main__":
    test_sd_card_timing()
