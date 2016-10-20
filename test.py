#!/usr/bin/python3

def removeMatches(str1, str2):
    if (str1.find(str2)==-1):
        return str1
    else:
        fi = str1.find(str2)
        sc = str1.find(str2, fi+len(str2))
        str1 = str1[:fi] + str1[(sc+len(str2)):]
        return removeMatches(str1,str2)


print(removeMatches('Ganteng ```GGG Halo``` ```Haha```', '```'))
