# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 22:13:55 2024

@author: kitty
"""


from plugins import Base

if __name__ == '__main__':
    for p in Base.plugins:
        inst = p()
        rules = inst.start()
        for rule in rules:
            print(rule)
