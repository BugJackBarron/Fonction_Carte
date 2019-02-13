# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 11:24:01 2019

@author: Fab-Tour
"""

from sympy import Symbol, pprint, sqrt
x=Symbol('x')


if __name__=='__main__' :
    print("""Voici un exemple d'utilisation avec enchainement :""")
    print("Commande : E=x+2")
    E=x+2
    pprint(E)
    print("Commande : E=3*E")
    E=3*E
    pprint(E)
    print("Commande : E=sqrt(E)")
    E=sqrt(E)
    pprint(E)