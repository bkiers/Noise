from utils import list_folders
from utils import prettify
from subject import Subject


class Category(object):

    def __init__(self, app, folder_name):
        self.folder_name = folder_name
        self.pretty_name = prettify(folder_name)
        self.subjects = Subject.list(app, self)
        self.image_path = "sounds/{0}/image.png".format(folder_name)

    def __str__(self):
        return "{0} ({1})".format(self.folder_name, len(self.subjects))

    @staticmethod
    def list(app):
        folders = list_folders(app, "sounds")
        return [Category(app, f) for f in folders]
