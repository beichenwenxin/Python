#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Author beichenwenxin https://github.com/beichenwenxin/Python/edit/master/greatest_common_divisor.py
Created on Fri Aug 24 18:00:09 2018
Work for greatest common divisor gcd
"""


def get_gcd(a,b):
    #print a,b
    if(a>b):
        i=a
        j=b
    else:
        i=b
        j=a
        
    m=i%j
    if m == 0 :
        return j
    else:
        return get_gcd(j,m)
        

if __name__ == '__main__':
    aa=get_gcd(123456,7890)
    print aa   
    
