import shutil
import subprocess
import tempfile
from typing import List


def skim(options: List = [], args: str = ""):
    if not shutil.which("sk"):
        print("skim not found in path")
    options_str = "\n".join(options)
    with tempfile.NamedTemporaryFile(mode="w", delete=True) as file:
        file.write(options_str)
        file.flush()
        command = "cat {filename} | sk {args}".format(filename=file.name, args=args)
        selected = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
        ).communicate()[0]
        return selected.decode("utf-8").strip().split("\n") if selected else ""
