import subprocess
import pytest

def run_command(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout.strip()

def test_rca_register():
    
    rca_path = "/sys/class/mmc_host/mmc0/mmc0:*/rca"
    
    # Fetch the RCA value
    rca_value = run_command(f"cat {rca_path}")
    
    if rca_value:
        print(f"RCA Register Output: {rca_value}")
    else:
        print("No RCA register found.")

if __name__ == "__main__":
    test_rca_register()
