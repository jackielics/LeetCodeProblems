#!/usr/bin/env python
# encoding: utf-8
"""
@author: JackLee
@file: 291_Maximum-Number-of-Substrings-Extracted.py
@time: 2023/7/11 22:24
@project: huawei-od-python
@desc: 291 最多提取子串数目
"""

def solution(A:list, B:list)->int:
	# ababcecfdc
	# abc
	res = 0
	ia  = ib = 0 # index of A and B
	while A: # not null
		if A[ia] == B[ib]:
			ib += 1 
			A.remove(A[ia])
		ia += 1


