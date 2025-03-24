import pytest

def parse_mmc_stat(stat_file):
    try:
        with open(stat_file, 'r') as f:
            data = f.read().strip().split()
        
        if len(data) < 17:
            raise ValueError("Unexpected data format in MMC stat file.")

        fields = [
            "Reads completed",
            "Reads merged",
            "Sectors read",
            "Time spent reading (ms)",
            "Writes completed",
            "Writes merged",
            "Sectors written",
            "Time spent writing (ms)",
            "I/Os in progress",
            "Time spent doing I/Os (ms)",
            "Weighted time spent on I/O (ms)",
            "Discard requests completed",
            "Discard requests merged",
            "Sectors discarded",
            "Time spent discarding (ms)",
            "Flush requests completed",
            "Time spent flushing (ms)"
        ]

        stats = {fields[i]: int(data[i]) for i in range(len(fields))}
        return stats
    except FileNotFoundError:
        print(f"Error: {stat_file} not found.")
        return None
    except ValueError as e:
        print(f"Error parsing file: {e}")
        return None


def test_mmc_statistics():
    stat_file = "/sys/class/mmc_host/mmc0/mmc0:4567/block/mmcblk0/stat"
    stats = parse_mmc_stat(stat_file)
    
    if stats:
        print("MMC Statistics:")
        for key, value in stats.items():
            print(f"{key}: {value}")
    
    assert stats is not None, "Failed to retrieve MMC statistics."
