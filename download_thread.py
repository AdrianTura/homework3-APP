from threading import Thread
from utils import download_file

class DownloadThread (Thread):
   def __init__(self, url, file_name):
      Thread.__init__(self)
      self.url = url
      self.file_name = file_name

   def run(self):
      download_file(self.url, self.file_name)