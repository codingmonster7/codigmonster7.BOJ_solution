# BOJ_2884

H, M = map(int,input().split())

if M - 45 < 0 and H >= 1: #분에서 45를 뺀 것이 0보다 작아지면
  H = H - 1
  result = M - 45
  M = 60 + result
  print(H,M,sep=' ')
elif M - 45 < 0 and H == 0:
  H = 23
  result = M - 45
  M = 60 + result
  print(H,M,sep=' ')
else:
  print(H,M-45,sep=' ')
