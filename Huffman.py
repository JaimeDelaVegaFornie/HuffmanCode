#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
"""
Practica 2 Geometria Computacional
"""

"""
Auxiliar para hacer print con colores, Si se ejecuta el código en la terminal funciona, en spyder no
"""

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

"""
Clase para crear el árbol
"""


class Nodo:
    def __init__(self,simbolo,frec,hi=None,hd=None):
        self.frec = frec
        
        self.simbolo = simbolo
        
        self.hi=hi
        
        self.hd=hd
        
        self.codigo = ''
        
        
        

"""
Funciones auxiliares para el script
"""        
        
        

def codigos(nodo,val=''):
        cod = dict()
        codigos_aux(nodo,cod,val='')
        return cod


def codigos_aux(nodo,cod,val=''):
    valor = val + str(nodo.codigo)
    if(nodo.hd):
        codigos_aux(nodo.hd,cod,valor)
    if(nodo.hi):
        codigos_aux(nodo.hi,cod,valor)
    
    if(not nodo.hi and not nodo.hd):
        cod[nodo.simbolo]=valor
    
    return cod
    

def frecuencias(text):
    tabla = dict()
    for char in text:
        if char in tabla:
            tabla[char]+=1
        else:
            tabla[char]=1
    return tabla


def decodificar(text,arbol):
    raiz = arbol
    decod = ''
    for i in text:
        if i=='0':
            arbol = arbol.hd 
        elif i=='1':
            arbol = arbol.hi
        if arbol.hi==None and arbol.hd==None:
            decod+=arbol.simbolo
            arbol=raiz
    return decod

def codificar(text,codigos):
    cod = ''
    for i in text:
        cod+=codigos[i]
    return cod

def longitud_media(codigos):
    valores = codigos.values()
    valores = [len(item) for item in valores]
    return sum(valores) / len(valores)


    

def normalizar(lista):
    result = []
    suma = sum(lista)
    for i in range(len(lista)):
        result.append(lista[i]/suma)
    return result
    
def arbol_Huffman(text):
    tabla = frecuencias(text)
    
    
    nodos = []    
    
    for simbolo in tabla.keys():
        nodos.append(Nodo(simbolo,tabla.get(simbolo)))
    
    
    while len(nodos)>1:
        nodos=sorted(nodos,key=lambda x: (x.frec,x.simbolo))
        hd = nodos[0]
        hi = nodos[1]
        
        hd.codigo = 0
        hi.codigo = 1
        
        nodo = Nodo(hi.simbolo+hd.simbolo,hi.frec+hd.frec,hi,hd)
        
        nodos.remove(hd)
        nodos.remove(hi)
        nodos.append(nodo)
    
    return nodos[0] 


def L(frec,cod):
    W=0
    s=0
    frec = normalizar_dict(frec)
    for i in cod:
        aux=len(cod[i])
        s += aux * frec[i]
        W += frec[i]
    return W*s

def normalizar_dict(dic):
    res = dic
    suma = sum(list(res.values()))
    for i in res:
        res[i]=res[i]/suma
    return res
    
def entropia(list):
    s = 0 
    for i in list:
        s += i * math.log(i,2)
    return (-1)*s



    


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Inicio de la práctica

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
print(bcolors.OKGREEN+'-'*40+bcolors.ENDC)
print(bcolors.OKGREEN+bcolors.BOLD+'PRÁCTICA 2'+bcolors.ENDC)
print(bcolors.OKGREEN+'-'*40+bcolors.ENDC)

with open('GCOM2022_pract2_auxiliar_eng.txt', 'r',encoding="utf8") as file:
      text_eng = file.read()
    
print(bcolors.HEADER+'Muestra de texto en Inglés\n'+bcolors.ENDC,text_eng)
print(bcolors.HEADER+'Muestra de texto en Castellano\n'+bcolors.ENDC,text_eng)

print(bcolors.HEADER+'Apartado 1'+bcolors.ENDC,bcolors.HEADER+'\n----'*3+bcolors.ENDC)
print(bcolors.OKBLUE+'\n\n','Parte de S_eng'+bcolors.ENDC)
arb_en = arbol_Huffman(text_eng)
codigo_en=codigos(arb_en)

print(bcolors.OKCYAN+'Codigo de Huffman S_eng: '+bcolors.ENDC, codigo_en)


entropia_eng = entropia(normalizar(list(frecuencias(text_eng).values())))
print('H(C_Eng) = ',entropia_eng)


L_eng = L(frecuencias(text_eng),codigo_en)
print('L(C_eng) = ',L_eng)


print('Se verifica el primer teorema de Shannon:\n +bcolors.ENDC',entropia_eng,' <= ',L_eng,' < ',entropia_eng+1)

print(bcolors.OKBLUE+'\n\n','Parte de S_esp'+bcolors.ENDC)

with open('GCOM2022_pract2_auxiliar_esp.txt', 'r',encoding="utf8") as file:
      text_esp = file.read()


arb_es = arbol_Huffman(text_esp)

codigo_es = codigos(arb_es)

   
print(bcolors.OKCYAN+'Codigo de Huffman S_esp: '+bcolors.ENDC, codigo_es)

entropia_esp = entropia(normalizar(list(frecuencias(text_esp).values())))
print('H(C_Esp) = ',entropia_esp)


L_esp = L(frecuencias(text_esp),codigo_es)
print('L(C_Esp) = ',L_esp)

print(bcolors.WARNING+'Se verifica el primer teorema de Shannon:\n '+bcolors.ENDC,entropia_esp,' <= ',L_esp,' < ',entropia_esp+1)



print(bcolors.HEADER+'\n----'*3+bcolors.ENDC)
print(bcolors.HEADER+'\n\nApartado 2'+bcolors.ENDC,bcolors.HEADER+'\n----'*3+bcolors.ENDC)
palabra = 'medieval'
palabra_cod = codificar(palabra, codigo_en)
print('Código para la palabra "medieval" utilizando S_Eng: ',palabra_cod)
print('Longitud de codificación: ',len(palabra_cod))
palabra_cod = codificar(palabra, codigo_es)
print('\n\nCódigo para la palabra "medieval" utilizando S_Esp: ',palabra_cod)
print('Longitud de codificación: ',len(palabra_cod))




print(bcolors.HEADER+'\n----'*3+bcolors.ENDC)
print(bcolors.HEADER+'\n\nApartado 3'+bcolors.ENDC)
print(bcolors.HEADER+'\n----'*3+bcolors.ENDC)
palabra = '10111101101110110111011111'
palabra_decod=decodificar(palabra,arb_en)
print('Palabra decodificada: ',palabra_decod)
nueva=codificar('hello', codigo_en)
nueva_decod=decodificar(nueva, arb_en)
print('Codificación de la palabra "Hello": ',nueva)
print('Descodificación de ',nueva,': ',nueva_decod)
print(bcolors.HEADER+'\n----'*3+bcolors.ENDC)



print(bcolors.HEADER+'\n\nExtra para la conclusión'+bcolors.ENDC)
print('Espacio ocupado por el mensaje inicial en castellano:',len(text_esp)*8)
print('Espacio ocupado por el mensaje inicial en inglés:',len(text_eng)*8)
text_es_cod=codificar(text_esp, codigo_es)
text_en_cod=codificar(text_eng, codigo_en)
print('Tamaño del mensaje codificado en castellano: ',len(text_es_cod))
print('Tamaño del mensaje codificado en inglés: ',len(text_en_cod))
gan_esp=len(text_esp)*8-len(text_es_cod)
gan_eng=len(text_eng)*8-len(text_en_cod)
print('La ganancia obtenida a consecuencia de la compresión en castellano es: ',gan_esp)
print('La ganancia obtenida a consecuencia de la compresión en inglés es: ',gan_eng)      

print(bcolors.OKGREEN+'-'*40+bcolors.ENDC)
print(bcolors.OKGREEN+bcolors.BOLD+'FIN DE LA PRÁCTICA'+bcolors.ENDC)
print(bcolors.OKGREEN+'-'*40+bcolors.ENDC)
