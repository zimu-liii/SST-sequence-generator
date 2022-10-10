# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 15:30:04 2021

@author: muzi
"""

def subword(s1,s2):
    sub = True
    list1 = []
    for i in range(len(s1)):
        word1 = s1[i:i+5]
        list1.append(word1)
    for j in range(len(s2)-5):
        if s2[j:j+5] in list1:
            sub = False
            break
    return sub

def complement(s):
    dictDNA = {'A':'T','T':'A','C':'G','G':'C'}
    com = []
    for i in s:
        com.append(dictDNA[i])
    com.reverse()
    coms = ''.join(com)
    return coms

def main(s1,s2):
    sub = subword(s1,s2)
    resub = subword(s1,complement(s2))
    ortho = sub and resub
    return ortho
