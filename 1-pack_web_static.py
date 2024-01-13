#!/usr/bin/python3
'''
script that generates a .tgz archive from the contents of the web_static using function do_pack
'''
from fabric.decorators import runs_once
from fabric.api import local
from datetime import datetime

def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""
    local("mkdir -p versions")
    path = ("versions/web_static_{}.tgz"
            .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))
    archive_result = local("tar -cvzf {} web_static"
                   .format(path),
                   capture=True)

    if archive_result.failed:
        return None
    return path
    
