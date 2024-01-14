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

    data_path = '/data/web_static/releases/'
    tmp = archive_path.split('.')[0]
    name = tmp.split('/')[1]
    dest = data_path + name

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, '/tmp')
        # Create the destination directory on the web server
        run('mkdir -p {}'.format(dest))
        # Extract the archive to the destination directory
        run('tar -xzf /tmp/{}.tgz -C {}'.format(name, dest))
        # Remove the archive from the web server
        run('rm -f /tmp/{}.tgz'.format(name))
        # Move the contents of web_static to the destination directory
        run('mv {}/web_static/* {}/'.format(dest, dest))
        # Remove the original web_static directory
        run('rm -rf {}/web_static'.format(dest))
        # Delete the symbolic link /data/web_static/current
        run('rm -rf /data/web_static/current')
        # Create a new symbolic link /data/web_static/current
        # pointing to the deployed directory
        run('ln -s {} /data/web_static/current'.format(dest))
        return True
    except Exception:
        return False
