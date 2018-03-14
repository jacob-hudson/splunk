#!/usr/bin/env python

import os
import shutil

shutil.copy2('savedsearches.conf', 'savedsearches-backup.conf')


with open('s-test.conf', 'r') as r, open('tmp.conf', 'w') as w:
    lines = r.readlines()
    for line in lines:
        if line.startswith('search')
            line = line.strip() + ' | where `More search info here`
            print line
            w.write(line)
        else:
            w.write(line)

os.rename('tmp.conf', 'savedsearches.conf')
