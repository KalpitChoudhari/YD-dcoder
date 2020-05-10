 
#declaring a dictionary with the number as key and letter as value
d= {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',
9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',
16:'p',17:'q',18:'r',19:'s',20:'t',21:'u',22:'v',
23:'w',24:'x',25:'y',26:'z'}

#accepting input
N = int(input())
a = [None for x in range(N)]

#assigning character in the list
for i in range((N-1),-1,-1):
  a[i] = d[N-i]

  
print(*a,sep="")



