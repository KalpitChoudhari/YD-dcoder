N = int(input())
add =0
greater =0
s = input()
d = s.split()

for i in range(len(d)):
  add = add+int(d[i])
  if(greater < int(d[i])):
    greater = int(d[i])

print(add%greater)
  