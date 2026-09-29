"""ADIF File to an excel spreadsheet for QSL label printing."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("adif2excel")
except PackageNotFoundError:  # not installed, e.g. a bare source checkout
    __version__ = "0.1.0+dev"

__all__ = ["__version__"]
