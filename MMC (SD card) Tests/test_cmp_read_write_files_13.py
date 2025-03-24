import subprocess
import pytest

MMC_DEVICE = "/dev/mmcblk0"
TEST_FILE = "/tmp/mmc_test_file"
MMC_COPY = "/mnt/mmc_test_copy"  # Adjust mount point if needed

def run_command(cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return e.stdout.strip() + e.stderr.strip()

@pytest.fixture(scope="module", autouse=True)
def setup_teardown():
    run_command(f"dd if=/dev/urandom of={TEST_FILE} bs=1M count=5")  # Generate 5MB random data
    yield
    run_command(f"rm -f {TEST_FILE} {MMC_COPY}")  # Cleanup after test

def test_mmc_data_integrity_cmp():
    try:
        # Write test file to MMC
        run_command(f"sudo dd if={TEST_FILE} of={MMC_DEVICE} bs=1M count=5 status=progress")
        
        # Read it back
        run_command(f"sudo dd if={MMC_DEVICE} of={MMC_COPY} bs=1M count=5 status=progress")

        # Compare files using cmp
        output = run_command(f"cmp -l {TEST_FILE} {MMC_COPY}")

        if not output:
            print("CMP Output: Files are identical.")
        else:
            print(f"CMP Output: Files differ. Differences:\n{output}")

        # Fail the test if there is any difference
        assert not output, "Data mismatch detected!"

    except Exception as e:
        pytest.fail(f"Error in MMC data integrity test (cmp): {e}")
