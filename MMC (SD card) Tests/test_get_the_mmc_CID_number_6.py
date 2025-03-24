import subprocess
import pytest

def run_command(cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return e.stdout.strip() + e.stderr.strip()

def test_mmc_cid():
    try:
        output = run_command("cat /sys/class/mmc_host/mmc0/mmc0*/cid")
        print(f"MMC CID: {output}")
        assert len(output) > 0, "MMC CID not readable"
    except Exception as e:
        pytest.fail(f"Error reading MMC CID: {e}")
