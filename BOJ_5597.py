# BOJ_5597

a = []

for i in range(30):
  a.append(i+1)           # a리스트 원소 1~30까지 넣기

for i in range(28):       # a리스트 원소에서 입력받은값 빼기
  a.remove(int(input()))  # 리스트이름.remove(값)

print(min(a),max(a),sep="\n")
