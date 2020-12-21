#!/usr/bin/env python3
"""Install `bash_profile` settings into shell profile paths.

Run from anywhere.
"""
from typing import List
from pathlib import Path as _Path
from pathlib import PosixPath as _PosixPath

SOURCEABLE_SCRIPT = [
    _PosixPath.home() / ".bash_profile",
    _PosixPath.home() / ".bashrc",
]


def install_sourceable_scripts(file_path: List[_Path]):
    for path in SOURCEABLE_SCRIPT:
        _install_sourceable_script(path)


def _install_sourceable_script(file_path: _Path):
    with open(file_path, "a") as f:
        source_command = "\nsource $HOME/bash_profile/bash_profile\n"
        f.write(source_command)


if __name__ == "__main__":
    import argparse
    print(SOURCEABLE_SCRIPT)

    description = (
        __doc__ + " Install locations: " +
        str(SOURCEABLE_SCRIPT)
    )
    parser = argparse.ArgumentParser(
        description=description,
    )
    _ = parser.parse_args()
    install_sourceable_scripts(SOURCEABLE_SCRIPT)
