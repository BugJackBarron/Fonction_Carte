# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 11:57:49 2019

@author: Fab-Tour
"""
from sympy.parsing.sympy_parser import parse_expr
import sympy as sp



class Carte(object):
    
    def __init__(self, Id, Value, ctype,Image=None) :
        """Initialisation de l'objet. 
        Id correspond au numéro de carte,
        Value à sa valeur ( sous forme de chaine de caratère)
        Image n'est pas utilisé pour l'instant
        ctype correspond au type de carte ( opération, opérateur ou fonction)"""
        self.Id=Id
        self.Value = Value
        self.Image=Image
        self.ctype=ctype
    
    def __str__(self):
        """Affichage amélioré du contenu d'une carte"""
        return """Carte id : {Id} Valeur :{Value} Type {ctype}\n""".format(
                Id=self.Id,Value=self.Value,ctype=self.ctype)
        
    def Compose(self,*expression):
        """fonction permettant la composition de la carte avec une ou 
        des expressions précédemment établies, dépend de l'attribut ctype 
        de la carte. Les expressions ne sont pas évaluées pour garder la trace
        de l'ordre des cartes."""
        if (len(expression)==1) and (self.ctype=='operation'):
            express=str(expression[0])
            return parse_expr("("+express+")"+self.Value,evaluate=False)
        elif (len(expression)==2) and (self.ctype=="operateur") :
            return parse_expr("("+str(expression[0])+")"
                    +self.Value+"("+str(expression[1])+")",evaluate=False)
        else :
            """Il faudra traiter une erreur dans ce cas"""
            pass
            
class Expression(object):            
        def __init__(self,symbole_base):
            """Initialisation de l'objet Expreesion. Par défaut, il faut lui
            fournir une chaine de caractère qui sera la variable utilisée.
            L'expression par défaut est l'identité."""
            self.x=sp.Symbol(symbole_base)
            self.expr=self.x
            
        def _gen(self,liste) :
            """Méthode interne à la classe de traitement des cartes. 
            Règles utilisée :
                1) On lit la liste de gauche à droite, et on compose tant qu'on
                ne tombe pas sur une carte opérateur ( numéro >=100)
                2) Si on tombe sur un opérateur, les cartes suivantes forment
                elle-même une nouvelle expression, qu'on tratite avec les règles
                ici établies.
            Il est bien sûr possible de modifier les règles, mais il faut 
            changer le code de génération ici."""
            for i,c in enumerate(liste) :
                if c>=100 :
                    E=Expression(str(self.x))
                    return cartes[c].Compose(self.expr,E._gen(liste[i+1:]))
                else :
                    self.expr=cartes[c].Compose(self.expr)
            return self.expr
            
                
            
        
            
        def genere_expr(self,*liste_carte) :
            """Génère une expression à partir d'une liste de carte, présentée
            soit sous la forme d'un tuple ou array, soit donnée comme une liste
            d'entiers."""
            if (len(liste_carte)==1 and isinstance(liste_carte[0],str)):
                
                liste_carte=[int(a) for a in liste_carte[0].strip("/n").split(" ")]
            self.expr=self._gen(liste_carte)
                
        def simplifie(self):
            """Renvoie une expression simplifiéede l'attribut expr"""
            return sp.simplify(self.expr)
                
               
                
                
    
if __name__=="__main__" :
    x=sp.Symbol('x')
    cartes ={}
    for i in range(1,10) :
        cartes[i]=Carte(i,"+{}".format(i),'operation')
        cartes[10+i]=Carte(10+i,"-{}".format(i),'operation')
        cartes[20+i]=Carte(20+i,"*{}".format(i),'operation')
        cartes[30+i]=Carte(30+i,"*(-{})".format(i),'operation')
        cartes[40+i]=Carte(40+i,"/{}".format(i),'operation')
        cartes[50+i]=Carte(50+i,"/(-{})".format(i),'operation')
    cartes[100]=Carte(100,"+",'operateur')
    cartes[200]=Carte(200,"-",'operateur')
    cartes[300]=Carte(300,"*",'operateur')
    cartes[400]=Carte(400,"/",'operateur')
    cartes[500]=Carte(500,"**",'operateur')
    print("""Les cartes sont définies par leur numéro :
        1=>9 : Addition du nnombre correspondant ;
        11=>19 : Soustraction du nombre correspondant au chiffre des unités ;
        21=>29 : Multiplication par le chiffre des unités ;
        31=>39 : Multiplication par l'opposé du chiffre des unités ;
        41=>49 : Division par le chiffre des unités ;
        51=>59 : Division par l'opposé du chiffre des unités ;
        100 : Opérateur additif ;
        200 : Opérateur soustractif ;
        300 : Opérateur multiplicatif ;
        400 : Opérateur fractionnaire ;
        500 : Opérateur d'exponentiation.
        """)
    lst_carte=input("Entrez la liste des cartes (avec des espaces entre chaque ): ")
    E=Expression('x')
    E.genere_expr(lst_carte)
    print("Expression obtenue avec les cartes dans l'ordre : ")
    sp.pprint(E.expr)
    print("Expression simplifiée : ")
    sp.pprint(E.simplifie())
    