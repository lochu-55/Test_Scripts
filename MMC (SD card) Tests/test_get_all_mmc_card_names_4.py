import subprocess
import pytest
import glob
import os

def run_command(cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return e.stdout.strip() + e.stderr.strip()

def get_all_mmc_card_names():
    card_names = []
    try:
        mmc_hosts = glob.glob("/sys/class/mmc_host/mmc*")  # Find all MMC hosts
        for host in mmc_hosts:
            mmc_cards = glob.glob(f"{host}/mmc*:*")  # Find all MMC cards under each host
            for card in mmc_cards:
                name_file = os.path.join(card, "name")
                if os.path.exists(name_file):
                    with open(name_file, "r") as f:
                        card_names.append(f.read().strip())
        return card_names if card_names else ["No MMC/SD cards detected"]
    except Exception as e:
        return [f"Error reading card names: {e}"]

def test_mmc_cards_detected():
    try:
        card_names = get_all_mmc_card_names()
        print(f"Detected MMC Card Names: {card_names}")
        assert "No MMC/SD cards detected" not in card_names, "No MMC/SD cards found"
    except Exception as e:
        pytest.fail(f"Error detecting MMC cards: {e}")
