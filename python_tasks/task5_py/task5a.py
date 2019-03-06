"""This module is for creating script for calculation actions: + - * /.
Script should return calculated result like: 2+6=8
"""
import sys


b = float(sys.argv[3])
a = float(sys.argv[1])

if sys.argv[2] == '/' and b == 0:
    action = {'/': 'Zero division'}
else:
    action = {
        '+': a+b,
        '-': a-b,
        '/': a/b,
        '*': a*b
    }


result = action[sys.argv[2]]

print(str(a)+sys.argv[2]+str(b)+'='+str(result))
