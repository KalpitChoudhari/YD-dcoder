#Accepting inputs
n = int(input())
s = input()

#String to list conversion
d = list(s)

#Making group of three characters
for i in range(n):
  d[i] = d[i]*3
  
print(*d,sep='')