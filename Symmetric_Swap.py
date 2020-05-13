"""
Author:Yadynesh-Nandane
Program for Symmetric Swap

"""

#Accepting Input
N = int(input())
s = input()
d = s.split(' ')

#Swapping of numbers having symmetric positions
#i.e Swaping 1st position number from top and 1st position number from bottom of the list
for i in range(0,N//2):
  d[i],d[N-(i+1)] = d[N-(i+1)],d[i]
  

print(*d,sep=' ')
