# -*- coding: utf-8 -*-
"""w10ppa6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x7_M042zwV55DlTaoCavvHK0c0t9-2UP
"""

class Country:
    '''
    Consider a class named Country that is defined in the prefix code.
    Your task is to create a list of objects of type Country.

    The first line of input is a positive integer nn that denotes the number of countries. 
    n blocks of input follow. Each block of input will have two lines; 
    the first line will be the name of the country and the second line will be its capital.

    Corresponding to each block, create an object of type Country. Append each object to a list named countries. 
    That is, each element of the list should be an object of type Country.


    '''
    def __init__(self):
        self.name = None
        self.capital = None

    def set_name(self, name):
        self.name = name

    def set_capital(self, capital):
        self.capital = capital

    def display(self):
        print(f'{self.capital} is the capital of {self.name}')

n = int(input())
countries = []
for i in range(n):
    C = Country()
    C.set_name(input())
    C.set_capital(input())
    countries.append(C)
print(countries)