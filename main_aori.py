from utils import ReleaseGetter
import os


if __name__ == '__main__':
    g = ReleaseGetter()
    print("\n".join(g.releases_list_str))
    version = input("Type one from releases above (full title): ")
    print("Downloading to:", os.getcwd())
    g.download(version)
    print("Successfully downloaded to: ", os.getcwd())
