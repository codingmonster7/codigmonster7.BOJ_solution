# BOJ_2480

a = list(map(int,input().split()))

if a[0] == a[1] == a[2]:
  print(10000 + a[0] * 1000)
elif a[0] == a[1] and a[0] != a[2]:
  print(1000 + a[0] * 100)
elif a[1] == a[2] and a[1] != a[0]:
  print(1000 + a[1] * 100)
elif a[2] == a[0] and a[2] != a[1]:
  print(1000 + a[2] * 100)
elif a[0] != a[1] and a[1] != a[2] and a[2] != a[0]: 
  print(max(a) * 100)
