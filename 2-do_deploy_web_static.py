#!/usr/bin/python3
'''
Fabric script that distributes an archive to web servers
using the function do_deploy.
'''
from fabric.api import env, put, run, sudo
from os.path import exists
from fabric.contrib import files


env.hosts = ['54.165.52.121', '34.204.81.17']


def do_deploy(archive_path):
    """
    Creates a tar gzipped archive from the web_static directory
    """
    if not os.path.exists(archive_path):
        return False
    
    file_name = os.path.basename(archive_path)
    folder_name = file_name.replace(".tgz", "")
    folder_path = "/data/web_static/releases/{}/".format(folder_name)
    success = False
    try:
        put(archive_path, "/tmp/{}".format(file_name))
        run("mkdir -p {}".format(folder_path))
        run("tar -xzf /tmp/{} -C {}".format(file_name, folder_path))
        run("rm -rf /tmp/{}".format(file_name))
        run("mv {}web_static/* {}".format(folder_path, folder_path))
        run("rm -rf {}web_static".format(folder_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder_path))
        print('New version deployed!')
        success = True
    except Exception:
        success = False
    return success
