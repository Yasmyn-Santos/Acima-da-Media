def maiores(lista, n): #nesse exercício não se pode usar o FOR e o WHILE (exigências do professor)
    '''Dada uma lista de números inteiros e um número inteiro n, 
    retorna outra lista que contém todos os elementos da lista 
    original maiores que n, ordenadas em ordem crescente.''' 
    lista.append(n) 
    lista.sort() 
    i = lista.index(n) 
    
    return lista[i+1:] 

import math
def acima_da_media(notas): 
    '''Dada uma lista com as notas dos alunos de uma turma, retorne 
    uma lista ordenada com as notas que ficaram acima da média.'''
    n = sum(notas) / len(notas)
    
    return maiores(notas, math.floor(n)+1)
   
