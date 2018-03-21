#!/usr/bin/env python

import os
import shutil

shutil.copy2('savedsearches.conf', 'savedsearches-backup.conf')
multiline = False
group = "none"

with open('savedsearches.conf', 'r') as r, open('tmp.conf', 'w') as w:
    lines = r.readlines()
    for i, line in enumerate(lines):

        # get next line
        try:
            next_line = lines[i+1]
        except IndexError: #end of file
            next_line = "EOF"

        if line.startswith('|') and not next_line.startswith('|') and multiline == True:
            # end of multiline search`
            w.write(line)
        elif line.startswith('search') and (next_line.startswith('|') or next_line.startswith('[')):
            # multiline search
            w.write(line)
        elif line.startswith('search') and not next_line.startswith('|') and not next_line.startswith('['):
            # simple search
            line = line.strip() + ' | where `suppression info goes here`\n'
            w.write(line)
        else:
            # not a search line at all
            w.write(line)


os.rename('tmp.conf', 'savedsearches.conf')
