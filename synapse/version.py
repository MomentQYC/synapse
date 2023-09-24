import platform

from matrix_common.versionstring import get_distribution_version_string

from synapse.config.server import ServerConfig

SYNAPSE_VERSION = get_distribution_version_string("matrix-synapse", __file__)


def getPythonVersion() -> str:
    hide_python_version = False
    if not ServerConfig.read_config(hide_python_version):
        return platform.python_version()
    else:
        return "UNKNOWN"


PYTHON_VERSION = getPythonVersion()
