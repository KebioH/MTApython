# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 14:22:03 2021

@author: MTAEXAM
"""

scort = []
while True:
    inscort = int(input("分數"))
    if inscort == "":
        break
    else:
        scort.append(inscort)
        scort2 = sorted(scort,reverse = True)
        scort.sort()
        scort.reverse()
        print(scort2)
        
         