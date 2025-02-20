#!/usr/bin/python3
'''
Fabric script(based on the file 1-pack_web_static.py)
that distributes an archive to your web servers,
using the function do_deploy
'''
from os import path
from fabric.api import env, put, run

env.hosts = ['34.224.1.205', '107.23.61.147']


def do_deploy(archive_path):
    """
    copies archive file from local to my web servers
    """

    if not path.exists(archive_path):
        return False
    try:
        file_name = archive_path.split("/")[-1].split(".")[0]
        put(archive_path, "/tmp/")

        run("mkdir -p /data/web_static/releases/{}".format(file_name))

        run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/"
            .format(file_name, file_name))

        run('rm -rf /tmp/{}.tgz'.format(file_name))

        run(('mv /data/web_static/releases/{}/web_static/* ' +
            '/data/web_static/releases/{}/')
            .format(file_name, file_name))

        run('rm -rf /data/web_static/releases/{}/web_static'
            .format(file_name))

        run('rm -rf /data/web_static/current')

        run(('ln -s /data/web_static/releases/{}/' +
            ' /data/web_static/current')
            .format(file_name))
        return True
    except Exception:
        return False
