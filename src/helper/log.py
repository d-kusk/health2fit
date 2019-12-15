from logging import getLogger, StreamHandler, DEBUG


class Log(object):
    def __init__(self, *args):
        self.log = getLogger(__name__)
        self.configure()

    def getInstance(self):
        if not self.log:
            self.log = self.__init__
        return self.log

    def configure(self):
        self.handler()
        self.log.propagate = False

    def handler(self):
        handler = StreamHandler()
        handler.setLevel(DEBUG)
        self.log.addHandler(handler)

    def loglevel(self):
        self.log.setLevel(DEBUG)
