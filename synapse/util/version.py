import platform

from matrix_common.versionstring import get_distribution_version_string

from synapse.config.homeserver import HomeServerConfig

hs_config = HomeServerConfig()

SYNAPSE_VERSION = get_distribution_version_string("matrix-synapse", __file__)


class Python_Ver:
    def __init__(self, hs_config) -> None:
        self.config = hs_config.config

    def getPythonVersion(self) -> str:
        if not self.config.server.hide_python_version:
            return platform.python_version()
        else:
            return "UNKNOWN"


def get_python_version() -> str:
    return Python_Ver(hs_config).getPythonVersion()


PYTHON_VERSION = get_python_version()