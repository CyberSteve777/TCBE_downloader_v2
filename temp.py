from github import Github
import re


releases_list = list(Github("CyberSteve777", "5Earth!5").get_user("Ryorama").get_repo(
            "TerrariaCraft-Bedrock").get_releases())
for e in releases_list:
    url = e.raw_data['assets'][0]['browser_download_url']
    print(re.match('https://github.com/(.+)/(.+)/(.+)/(.+)/(.+)/(.+)', url).groups())
