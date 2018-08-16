from utils import list_folders
from sound import Sound
from utils import prettify


class Subject:

    def __init__(self, app, category, folder_name):
        self.category = category
        self.folder_name = folder_name
        self.pretty_name = prettify(folder_name)
        self.sounds = Sound.list(app, self)
        self.image_path = "sounds/{0}/{1}/image.png".format(category.folder_name, folder_name)

    def __str__(self):
        return "{0} ({1})".format(self.folder_name, len(self.sounds))

    @staticmethod
    def list(app, category):
        folders = list_folders(app, "sounds/{0}".format(category.folder_name))
        return [Subject(app, category, f) for f in folders]
