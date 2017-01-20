#!/usr/bin/env python3
# vim: ft=python
# # -*- coding: UTF-8 -*-"
# ------------------------------------------------
#   Creation Date:    20-01-2017
#     Last Change: ter 29 nov 2016 09:21:52 BRT
# this script aim:  <+this script aims+>
#          author:  sergio luiz araujo silva
#            site:  http://vivaotux.blogspot.com
#         twitter:  @voyeg3r
# ------------------------------------------------

# source: https://gist.github.com/igniteflow/1226919

import os

"""
Renames the filenames within the same directory to be Unix friendly
(1) Changes spaces to hyphens
(2) Makes lowercase (not a Unix requirement, just looks better ;)
Usage:
python rename.py
"""

path =  os.getcwd()
filenames = os.listdir(path)

for filename in filenames:
    os.rename(filename, filename.replace(" ", "-").lower())


