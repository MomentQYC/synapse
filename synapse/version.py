import platform

from matrix_common.versionstring import get_distribution_version_string

from synapse.config.server import ServerConfig

SYNAPSE_VERSION = get_distribution_version_string("matrix-synapse", __file__)

sv_config = ServerConfig()

def getPythonVersion() -> str:
    sv_config.read_config(sv_config)
    if not sv_config.hide_python_version:
        return platform.python_version()
    else:
        return "UNKNOWN"


PYTHON_VERSION = getPythonVersion()
