# -*- coding: utf-8 -*-
"""depthof paranthesis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eTf40H_w8PbZPLGnuNFsmXYe68Q_fzN0
"""

def depth(word):
    open = []
    count = 0
    for i in range(len(word)):
        if word[i] == '(':
            open.append(i)
        elif word[i] == ')':
            if count < len(open):
                count = len(open)
            open.pop()
    return count
depth('(()(()))()')