import site
import os
from os import path

VENDOR = path.join(path.abspath(path.dirname(__file__)), '_vendor')
PACKAGES = [
    path.join(VENDOR, pth) for pth in os.listdir(VENDOR)
    if path.isdir(path.join(VENDOR, pth)) and not pth.startswith('__')
]
for pkg in PACKAGES:
    site.addsitedir(pkg)
