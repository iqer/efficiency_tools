#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
!!!
Please put this file to the root path of the project
!!!
"""
import os


current_path = os.path.abspath(os.path.dirname(__file__))
for parent, dirnames, filenames in os.walk(current_path):
    for filename in filenames:
        try:
            pathfile = os.path.join(parent, filename)
            if pathfile == os.path.abspath(__file__):
                continue
            new_pathfile = os.path.join(parent, '{}.bak'.format(filename))
            fread = open(pathfile, 'r')
            fwrite = open(new_pathfile, 'w')
            count = 0
            for line in fread.readlines():
                if line:
                    if '© 2013-2019' in line:
                        line = line.replace('© 2013-2019', '© 2013-2020')
                        count += 1
                fwrite.write(line)
            print('Modify {} palces in the file: {}'.format(count, filename))
        finally:
            if locals().get('fread'):
                fread.close()
            if locals().get('fwrite'):
                fwrite.close()
        os.remove(pathfile)
        os.rename(new_pathfile, pathfile)
