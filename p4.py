# File:    p4.py
# Author:  Yongqiang Zhou
# Date:    Tue Jan 27 18:32:33 CST 2015
# Desc:    https://projecteuler.net/problem=4

palin_num_array = [str(i)+str(i)[::-1] for i in range(998, 99, -1)]

found = False
for palin_num in palin_num_array:
    # TODO: Optimization for even and odd
    for factor in range(100, 999):
        if int(palin_num)%factor ==0 and 100 <= int(palin_num)/factor <= 998:
            print palin_num, factor, int(palin_num)/factor
            found = True
            break
            
    if found:
        break
