import platform

from matrix_common.versionstring import get_distribution_version_string

from synapse.config.server import ServerConfig

sv_config = ServerConfig()

SYNAPSE_VERSION = get_distribution_version_string("matrix-synapse", __file__)


class Python_Ver:
    def __init__(self, sv_config) -> None:
        self.config = sv_config.config

    def getPythonVersion(self) -> str:
        if not self.config.hide_python_version:
            return platform.python_version()
        else:
            return "UNKNOWN"


def get_python_version() -> str:
    return Python_Ver(sv_config).getPythonVersion()


PYTHON_VERSION = get_python_version()
