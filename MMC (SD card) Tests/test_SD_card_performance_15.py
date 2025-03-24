import pytest
import subprocess
import json

def run_fio_test(name, filename, rw, bs, size, runtime, numjobs):
    cmd = [
        "sudo", "fio",
        f"--name={name}",
        f"--filename={filename}",
        f"--rw={rw}",
        f"--bs={bs}",
        f"--size={size}",
        f"--runtime={runtime}",
        f"--numjobs={numjobs}",
        "--time_based",
        "--output-format=json"
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return json.loads(result.stdout)



@pytest.mark.parametrize("test_params", [
    {"name": "mmc-randrw-test", "rw": "randrw", "bs": "4k", "size": "50M", "runtime": 10, "numjobs": 1},
    {"name": "mmc-seq-read", "rw": "read", "bs": "128k", "size": "100M", "runtime": 10, "numjobs": 1},
    {"name": "mmc-seq-write", "rw": "write", "bs": "128k", "size": "100M", "runtime": 10, "numjobs": 1}
])
def test_fio_mmc(test_params):
    filename = "/dev/mmcblk0"  # Update as needed
    output = run_fio_test(**test_params, filename=filename)

    print("FIO Test Output:")
    print(json.dumps(output, indent=4))  # Pretty-print JSON output
