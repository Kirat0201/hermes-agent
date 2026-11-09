"""The PATH directory an activated Windows shell gets for Git Bash.

Git for Windows' ``usr/bin`` carries coreutils that would shadow Windows'
``find``/``sort``, so the launcher-only ``bin`` beside it wins when present.
Host-independent: the function takes the resolved bash path as data.
"""
from pathlib import Path

from pm.shell import path_directory


def _touch(path: Path) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(b"")
    return str(path)


def test_usr_bin_bash_puts_the_launcher_bin_on_path(tmp_path):
    _touch(tmp_path / "Git" / "bin" / "bash.exe")
    assert path_directory(_touch(tmp_path / "Git" / "usr" / "bin" / "bash.exe")) == str(tmp_path / "Git" / "bin")


def test_usr_bin_bash_without_a_launcher_keeps_its_own_directory(tmp_path):
    bash = _touch(tmp_path / "msys64" / "usr" / "bin" / "bash.exe")
    assert path_directory(bash) == str(tmp_path / "msys64" / "usr" / "bin")
