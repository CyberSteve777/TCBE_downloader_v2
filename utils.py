from github import Github
import sys
import os
import time
import re
from urllib.request import *


def report_hook(count, block_size, total_size):
    global start_time
    if count == 0:
        start_time = time.time()
        return
    duration = time.time() - start_time + 0.000001
    progress_size = int(count * block_size)
    speed = int(progress_size / (1024 * duration))
    percent = int(count * block_size * 100 / total_size)
    if 100 >= percent >= 0:
        sys.stdout.write("\r{} %, {} KB, {} KB/s, {} seconds passed         ".format(
            percent, progress_size / 1024, speed, round(duration, 2)))
    else:
        sys.stdout.write("\r{} KB, {} KB/s, {} seconds passed         ".format(
            progress_size / 1024, speed, round(duration, 2)))
    sys.stdout.flush()


class ReleaseGetter:
    def __init__(self):
        self.releases_list = []
        self.releases_list_str = []
        self.release_link = {}
        self.update()

    def update(self):
        self.releases_list = list(Github().get_user("Ryorama").get_repo(
            "TerrariaCraft-Bedrock").get_releases())
        temp_r = set()
        self.releases_list_str.clear()
        for elem in self.releases_list:
            link = elem.raw_data['assets'][0]['browser_download_url']
            if elem.title not in temp_r:
                self.release_link[elem.title] = link
                self.releases_list_str.append(elem.title)
                temp_r.add(elem.title)

    def __iter__(self):
        for key, value in self.release_link:
            yield key, value

    def __str__(self):
        return "ReleaseGetter(releases=[" + ", ".join(r.title for r in self.releases_list) + "])"

    def download(self, release_title, path=os.getcwd()):
        url = self.release_link[release_title]
        splitter = re.match('https://github.com/(.+)/(.+)/(.+)/(.+)/(.+)/(.+)', url).groups()
        projectname, version = splitter[1], splitter[-2]
        filename = path + "/" + projectname + "-" + version
        zipfile_name = filename + ".zip"
        urlretrieve(url, zipfile_name, reporthook=report_hook)
        os.rename(zipfile_name, filename + ".mcaddon")
        print()
