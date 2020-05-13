n = int(input())
years = []

for i in range(n):
  years.append(int(input()))
  if(int(years[i])%4 == 0):
    if(int(years[i]%100 == 0)):
      if(int(years[i]%400 == 0)):
        print("Yes")
      else:
        print("No")
    else:
      print("Yes")
  else:
    print("No")