""" The Upload ServiceProvider for Backblaze B2 """

from masonite.provider import ServiceProvider
from .driver import UploadBackblazeDriver


class UploadBackblazeProvider(ServiceProvider):

    wsgi = False

    def register(self):
        self.app.bind('UploadB2Driver', UploadBackblazeDriver)

    def boot(self):
        pass
