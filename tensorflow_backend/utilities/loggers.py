import logging
import os
from django.utils import timezone


class DailyFileHandler(logging.FileHandler):
    def __init__(self, filename, *args, **kwargs):
        self._day = timezone.localtime(timezone.now()).date()
        self._filename = filename
        self.mkdir(filename)
        filename = '%s.%s' % (self._filename, self._day)
        super(DailyFileHandler, self).__init__(filename, *args, **kwargs)

    @staticmethod
    def mkdir(filename):
        folder = os.path.dirname(filename)
        if not os.path.exists(folder):
            os.makedirs(folder)

    def emit(self, record):
        day = timezone.localtime(timezone.now()).date()
        if self._day != day:
            self._day = day
            self.close()
            self.baseFilename = '%s.%s' % (self._filename, self._day)
        super(DailyFileHandler, self).emit(record)
