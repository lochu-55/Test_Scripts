import subprocess
import pytest

def run_command(cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return e.stdout.strip() + e.stderr.strip()

def test_csd_register():
    csd_path = "/sys/class/mmc_host/mmc0/mmc0*/csd"
    output = run_command(f"cat {csd_path}")
    
    print(f"CSD Register Output: {output}")
    assert output, "CSD register is empty or not accessible."
