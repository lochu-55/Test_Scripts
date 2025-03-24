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

def test_mmc_data_integrity_md5():
    try:
        run_command(f"sudo dd if={TEST_FILE} of={MMC_DEVICE} bs=1M count=5")
        run_command(f"sudo dd if={MMC_DEVICE} of={MMC_COPY} bs=1M count=5")

        md5_original = run_command(f"md5sum {TEST_FILE}").split()[0]
        md5_mmc = run_command(f"md5sum {MMC_COPY}").split()[0]

        print(f"Original MD5: {md5_original}")
        print(f"MMC MD5: {md5_mmc}")

        assert md5_original == md5_mmc, "MD5 checksum mismatch! Data integrity compromised."
    except Exception as e:
        pytest.fail(f"Error in MMC data integrity test (md5sum): {e}")
