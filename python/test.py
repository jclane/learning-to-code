import os
from pathlib import Path

home = str(Path.home())
rootdir = os.path.join(home, 'bin')
fileslist = []

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        fileslist.append(file)

for el in fileslist:
    with open(os.path.join(rootdir, el), encoding='latin1') as f:
        for line in f:
            print(line)