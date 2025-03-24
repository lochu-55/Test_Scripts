import subprocess
import pytest

def check_mmc_device_error():
    try:
        # Run dmesg to capture the kernel logs
        result = subprocess.run(["dmesg", "-T"], capture_output=True, text=True, check=True)
        
        # Filter out only the lines related to 'mmc' or 'sd'
        mmc_sd_logs = [line for line in result.stdout.splitlines() if "mmc" in line.lower() or "sd" in line.lower()]
        
        # Print filtered logs
        print("\nFiltered MMC/SD Logs:\n")
        for line in mmc_sd_logs:
            print(line)
        
        # Check for any errors or warnings related to MMC or SD devices
        if mmc_sd_logs:
            # Search for error messages related to MMC or SD
            if any("error" in line.lower() for line in mmc_sd_logs):
                return True  # Indicates error detected in MMC/SD logs
            else:
                return False  # No error found in MMC/SD logs
        else:
            return False  # No MMC/SD entries found in the logs

    except subprocess.CalledProcessError as e:
        raise Exception(f"Error while checking kernel logs: {e.stderr}")


def test_mmc_device_error_in_logs():
    
    # Run the function to check for MMC/SD errors in kernel logs
    error_found = check_mmc_device_error()

    # Check if errors were found in the logs and print the appropriate message
    if error_found:
        print("\nMMC/SD device error detected in kernel logs.")
    else:
        print("\nNo MMC/SD device errors found in kernel logs.")
