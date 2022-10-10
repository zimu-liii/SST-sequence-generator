# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 16:04:06 2021

@author: muzi
"""

import random
def seqgen(l):
    base = ['A','T','C','G']
    s = ''
    for i in range(l):
        s += random.choice(base)
    return s

def homorun(s):
    homo = True
    for i in range(0,len(s)-3):
        run = s[i:i+4]
        if run == run[0]*4:
            homo = False
            break
    return homo

def GCcontent(s):
    count = 0
    for i in s:
        if i == 'G' or i == 'C':
            count = count + 1
    GC = float(count/len(s))
    return GC

def main(l):
    while True:
        s = seqgen(l)
        homo = homorun(s)
        GC = GCcontent(s)
        if homo == True and 0.45 < GC < 0.55:
            return s
