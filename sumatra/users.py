"""
Find information about the current user
"""

from os.path import expanduser, join, exists
import json


def get_user(working_copy=None):
    """
    Find information about the current user, first trying ~/.smtrc, then
    the version control system
    """
    global_conf_file = expanduser(join("~", ".smtrc"))
    if exists(global_conf_file):
        with open(global_conf_file) as fp:
            config = json.load(fp)
        if "username" in config:
            return config["username"]
    if working_copy:
        return working_copy.get_username()
    return ''
