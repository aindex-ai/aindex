from .aindex import aindex as aindex

from importlib import metadata
# use the method from LangChain (Chase, H. (2022). LangChain [Computer software]. https://github.com/hwchase17/langchain) to get the version of the package
try:
    __version__ = metadata.version(__package__)
except metadata.PackageNotFoundError:
    # Case where package metadata is not available.
    __version__ = ""
del metadata  # optional, avoids polluting the results of dir(__package__)