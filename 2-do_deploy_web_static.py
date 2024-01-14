#!/usr/bin/python3
'''
Fabric script that distributes an archive to web servers using the function do_deploy.
'''
from fabric.api import env, put, run, sudo
from os.path import exists

env.hosts = ['54.165.52.121', '34.204.81.17']
#env.user = 'ubuntu' 
#env.key_filename = '<path_to_your_ssh_key>'  

def do_deploy(archive_path):
    """
    Distributes an archive to web servers using the function do_deploy.
    """
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, '/tmp/')

        # Extract the archive to /data/web_static/releases/<archive filename without extension>
        filename = archive_path.split("/")[-1]
        folder_name = filename.split(".")[0]
        remote_path = '/data/web_static/releases/'

        run('sudo mkdir -p {}{}'.format(remote_path, folder_name))
        run('sudo tar -xzf /tmp/{} -C {}{}/'.format(filename, remote_path, folder_name))

        # Remove the archive from the web server
        run('sudo rm /tmp/{}'.format(filename))

        # Delete the symbolic link /data/web_static/current
        run('sudo rm -rf /data/web_static/current')

        # Create a new symbolic link /data/web_static/current
        run('sudo ln -s {}{}/ /data/web_static/current'.format(remote_path, folder_name))

        print("New version deployed!")
        return True
    except Exception as e:
        print(e)
        return False
