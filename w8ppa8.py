# -*- coding: utf-8 -*-
"""w8ppa8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x7_M042zwV55DlTaoCavvHK0c0t9-2UP
"""

def non_decreasing(L):
    """
    A recursive function that determines if L is sorted in non-decreasing order

    Argument: 
        L: list of integers
    Return:
        result: bool
    """
    if len(L) == 1:
        return True
    if L[1] < L[0]:
        return False
    else:
        return non_decreasing(L[1:])
L = [10, 100, 99, 1000, 10000]
non_decreasing(L)

