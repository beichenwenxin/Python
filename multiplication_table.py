#!/usr/bin/python   

for i in range(1,10):
    for j in range(i):
        j += 1
        print ("%d * %d = %-2d  " %(j, i, i*j)),
    print ""
