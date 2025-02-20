#!/usr/bin/python3
'''
Fabric script that generates a .tgz archive
from the contents of the web_static folder
of your AirBnB Clone repo, using the function do_pack
'''
from datetime import datetime
from fabric.api import local


def do_pack():
    '''
    Function that converts a .tgz archive
    '''
    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file = "versions/web_static_{}.tgz".format(date)
    try:
        local("tar -cvzf {} web_static".format(file))
        return file
    except FileNotFoundError:
        return None
