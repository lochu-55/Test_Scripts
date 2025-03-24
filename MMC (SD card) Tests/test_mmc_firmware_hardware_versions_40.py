import os

def read_mmc_attribute(attribute):
    path = f"/sys/class/mmc_host/mmc0/mmc0:*/{attribute}"
    try:
        file_path = os.popen(f'ls {path}').read().strip()
        if not file_path:
            print(f"{attribute} file not found!")
            return None
        
        with open(file_path, 'r') as file:
            value = file.read().strip()
            print(f"{attribute}: {value}")
            return value
    except Exception as e:
        print(f"Error reading {attribute}: {e}")
        return None

def test_mmc_revisions():
    fwrev = read_mmc_attribute("fwrev")
    hwrev = read_mmc_attribute("hwrev")
    
    assert fwrev is not None, "Failed to read firmware revision"
    assert hwrev is not None, "Failed to read hardware revision"

if __name__ == "__main__":
    test_mmc_revisions()
