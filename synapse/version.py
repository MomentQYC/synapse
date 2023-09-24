import platform

from matrix_common.versionstring import get_distribution_version_string

from synapse.config.server import ServerConfig

SYNAPSE_VERSION = get_distribution_version_string("matrix-synapse", __file__)


class Python_Ver:
    def __init__(self) -> None:
        self.server_config = ServerConfig()

    def getPythonVersion(self) -> str:
        if not self.server_config.hide_python_version:
            return platform.python_version()
        else:
            return "UNKNOWN"


PYTHON_VERSION = Python_Ver.getPythonVersion()
