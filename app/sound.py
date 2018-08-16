from utils import list_mp3s
from utils import prettify


class Sound:

    def __init__(self, subject, file_name):
        self.subject = subject
        self.pretty_name = prettify(file_name)
        self.file_name = file_name
        self.file_path = "sounds/{0}/{1}/{2}".format(subject.category.folder_name, subject.folder_name, file_name)

    def __str__(self):
        return "{0}".format(self.file_name)

    @staticmethod
    def list(app, subject):
        folders = list_mp3s(app, "sounds/{0}/{1}".format(subject.category.folder_name, subject.folder_name))
        return [Sound(subject, f) for f in folders]
