# -*- coding: utf-8 -*-
"""
Created on Tue Jan 20 23:27:41 2026

@author: Acer
"""

class Cuzdan:
    def __init__(self, sahip, bakiye=0):
        self.sahip = sahip
        self.bakiye = bakiye
    def __repr__(self):
        return f"Sahip : {self.sahip},Bakiye : {self.bakiye}"
    def info(self):
        print(f"Sahip: {self.sahip} Bakiye : {self.bakiye} TL")
        
    def para_ekle(self, miktar):
        if miktar > 0:
            self.bakiye += miktar
            print(f"{miktar} Tl eklendi. Güncel Bakiye : {self.bakiye} TL")
        else:
            print("Eklenecek bakiye pozitif olmalı.")
            
    def para_harcama(self,miktar):
        if miktar <= self.bakiye:
            self.bakiye -= miktar
            print((f"{miktar} TL harcandı. Güncel Bakiye : {self.bakiye} TL"))
        else:
            print("YETERSİZ BAKİYE")
            
class Altin_Hesabi(Cuzdan):
    def para_ekle(self, miktar):
        if miktar > 0:
           super().para_ekle(miktar * 1.10)
           print(f"{miktar} TL yatırıldı. (%10 Kazançla) Güncel bakiye : {self.bakiye} TL")
        else:
            print("Eklenecek bakiye pozitif olmalı")
            
c = Cuzdan("Beyza Özge",100000)
c.para_ekle(50000)
c.para_harcama(75000)
c.info()
a = Altin_Hesabi("Beyza Özge",5000)
a.para_ekle(50000)
a.info()
print(c)
print(a)
    
    
            
        
   

         