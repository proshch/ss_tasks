"""This module is for creating script that sort data by conditions 
(index of sub list item in list of lists; dict key)"""


seq1 = [[3, 3, 8], [4, 5, 5], [8, 7, 9]]
seq2 = [{'ball': 3, 'apple': 5, 'red': 6}, {'ball': 4, 'red': 2, 'apple': 1}, {'ball': 4, 'red': 3, 'apple': 1}]

print(sorted(seq1, key=lambda seq1: seq1[2]))

print(sorted(seq2, key=lambda seq2: seq2['apple']))
