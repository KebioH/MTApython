# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 15:01:09 2021

@author: MTAEXAM
"""
f = open("9999.txt","r")
for line in f:
    print(line)
f.close()
with open("9999.txt","r") as f:
    for line in f:
        print(line)