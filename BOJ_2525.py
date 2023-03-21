# BOJ_2525

H, M = map(int,input().split())
C = int(input())

if M + C >= 60:
  H = H + (M + C) // 60
  if H >= 24:
    H = H - 24
    print(H, (M+C)%60, sep = ' ')
  else:
    print(H, (M+C)%60, sep = ' ')
else:
  print(H, M + C, sep = ' ')
