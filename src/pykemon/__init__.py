from importlib.metadata import version

__version__ = version("pykemon")

from pykemon.CRUD.team_editor import team_editor

from pykemon.db import get_connection
