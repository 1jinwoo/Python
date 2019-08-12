# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 03:02:27 2018

@author: Justin Won
"""

#!/usr/bin/env python

# run as python script

import argparse
import zipfile

class help:
    def __init__(self, zippath):
        self.zpath = zippath
        
        with zipfile.ZipFile(zippath) as zipf:
            self.zipf_names = zipf.namelist()
            self.zipf_data = dict()
            for file_name in self.zipf_names:
                with zipf.open(file_name) as file:
                    self.zipf_data[file_name] = list(str(zipf.read(file_name)).split('\\n')) # \\n because of *WINDOWS* 
                    
    def counts(self, substring):
        count = 0
        for name in self.zipf_names:
            for string in self.zipf_data[name]:
                if substring in string:
                    count += 1
        print(count)
        
    def files(self, substring):
        for name in self.zipf_names:
            count = 0
            for string in self.zipf_data[name]:
                if substring in string:
                    count += 1
            if count != 0:
                print("{} : {}".format(name, count))
    
    def grep(self, substring):
        for name in self.zipf_names:
            for i, string in enumerate(self.zipf_data[name]):
                if substring in string:
                    print("{}({}): {}".format(name, i, string))
                    

parser = argparse.ArgumentParser()

parser.add_argument("-c", "--counts", help="hits", type=str)

parser.add_argument("-g", "--grep", help="grep", type=str)

parser.add_argument("-f", "--files", help="files", type=str)


args = parser.parse_args()

zpath = r'C:\Users\justi\Downloads\python-3.7.1rc2-docs-text.zip'
h = help(zpath)


if args.counts:
    h.counts(args.counts)
    
if args.grep:
    h.grep(args.grep)
    
if args.files:
    h.files(args.files)



