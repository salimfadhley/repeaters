import functools
import os
from pathlib import Path


def ensure_directory_exists(fn):
    @functools.wraps(fn)
    def wrapped(*args, **kwargs):
        result = fn(*args, **kwargs)
        assert isinstance(result, Path)
        result.mkdir(exist_ok=True)
        return result
    return wrapped

@ensure_directory_exists
def get_output_path() -> Path:
    try:
        return Path(os.environ["BUILD_DIRECTORY"])
    except KeyError:
        return Path(os.getcwd()) / "build"


def get_repeaters_csv_output_path() -> Path:
    return get_output_path() / "repeaters.csv"
