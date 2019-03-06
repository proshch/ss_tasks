"""This module is for creating script for calculation actions: + - * /.
Script should return calculated result like: 2+6=8
""" 
import argparse
from functools import reduce


parser = argparse.ArgumentParser()

parser.add_argument('-a', choices=('+', '-', '*', '/'), dest='sign', 
                    help='Choose action command')

parser.add_argument('-v', action='append', type=float, dest='numbers',
                    default=[],
                    help='Add repeated values to a list',
                    )

args = parser.parse_args()

num = args.numbers
if args.sign == '+':
    result = sum(num)
elif args.sign == '-':
    result = reduce((lambda x, y: x - y), num)
elif args.sign == '/' and 0 not in num[1:]:
    result = reduce((lambda x, y: x / y), num)
elif args.sign == '*':
    result = reduce((lambda x, y: x * y), num)
else:
    print("Try again")
    result=''

print(f'{args.sign}'.join([str(elem) for elem in num])+'='+str(result))

