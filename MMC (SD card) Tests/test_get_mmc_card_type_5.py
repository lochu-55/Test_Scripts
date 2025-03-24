import subprocess
import pytest

def run_command(cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return e.stdout.strip() + e.stderr.strip()

def test_mmc_card_type():
    try:
        output = run_command("cat /sys/class/mmc_host/mmc0/mmc0*/type")
        print(f"MMC Card Type: {output}")
        assert output in ["SD", "MMC"], f"Unexpected MMC type: {output}"
    except Exception as e:
        pytest.fail(f"Error reading MMC type: {e}")
