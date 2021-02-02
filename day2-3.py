# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 15:32:44 2021

@author: MTAEXAM
"""

dictl = {'A':"內向穩重",'B':"外向樂觀",'O':"堅強自信",'AB':"聰明自然"}
blood = input("輸入血型:")
name = dict.get(blood)
if blood == None:
    print("沒有此血型")
else:
    print(name)
print(name)