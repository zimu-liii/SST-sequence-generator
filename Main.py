# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 16:19:39 2021

@author: muzi
"""

import SeqFilter as SF
import OrthoFilter as OF

def Main(l,n):
    slist = []
    while len(slist) < n:
        s = SF.main(l)
        sp = True
        if slist == []:
            slist.append(s)
        elif slist != []:
            for i in slist:
                sp = sp and OF.main(i,s)
            if sp == True:
                slist.append(s)
    return slist
