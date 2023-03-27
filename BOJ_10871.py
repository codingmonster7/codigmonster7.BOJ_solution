#BOJ_10871

N, X = map(int,input().split())
B = []
A = list(map(int,input().split()))
for i in A:      # A안에 있는 요소들 중에서
  if i < X:
    B.append(i)  #요소 한개를 추가하는 함수.

for i in B:
  print(i, end=" ")
