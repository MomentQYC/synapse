import platform

from matrix_common.versionstring import get_distribution_version_string

from synapse.config.server import ServerConfig

SYNAPSE_VERSION = get_distribution_version_string("matrix-synapse", __file__)


class Python_Ver:
    @classmethod
    def getPythonVersion(cls) -> str:
        if not ServerConfig.hide_python_version:
            return platform.python_version()
        else:
            return "UNKNOWN"


def get_python_version() -> str:
    return Python_Ver.getPythonVersion()


PYTHON_VERSION = get_python_version()
