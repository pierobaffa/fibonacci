# -*- coding: utf-8 -*-
"""fibonacci

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1l4LvphqDMQiiHqWMY84DdJMiOd5MXplQ
"""

def fibonacci(x,y):

  f = 0

  while (len(str(f)) != 1000):
    
    f = x + y
    x = y
    y = f

  return f

x = 0
y = 1

print(fibonacci(x,y))