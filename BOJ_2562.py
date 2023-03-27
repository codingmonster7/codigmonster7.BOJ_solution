#BOJ_2562

A = []

for i in range(9):
  A.append(int(input()))   리스트이름.append()
  
x = A.index(max(A))   # 리스트이름.index(값) 

print(max(A), x + 1, sep="\n")
