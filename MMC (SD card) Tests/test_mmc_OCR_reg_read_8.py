import subprocess
import pytest

def run_command(cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return e.stdout.strip() + e.stderr.strip()

def test_ocr_register():
    ocr_path = "/sys/class/mmc_host/mmc0/mmc0*/ocr"
    output = run_command(f"cat {ocr_path}")
    
    print(f"OCR Register Output: {output}")
    assert output, "OCR register is empty or not accessible."
