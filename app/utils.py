import os
import re


def list_folders(app, child):
    root = "{0}/{1}".format(app.static_folder, child)
    contents = os.listdir(root)
    folders = [x for x in contents if os.path.isdir(os.path.join(root, x))]
    folders.sort()
    return folders


def list_mp3s(app, child):
    root = "{0}/{1}".format(app.static_folder, child)
    contents = os.listdir(root)
    mp3s = [x for x in contents if os.path.isfile(os.path.join(root, x)) and x.lower().endswith(".mp3")]
    mp3s.sort()
    return mp3s


def prettify(folder_or_file_name):
    words = re.split(r'\W', re.sub(r'\.[mM][pP]3$', '', folder_or_file_name))
    return " ".join([str(x).capitalize() for x in words])
