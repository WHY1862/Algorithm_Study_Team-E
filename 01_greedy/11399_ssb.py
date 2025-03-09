n = int(input())
p = list(map(int, input().split()))
p.sort(reverse=True)

result = 0
for i, j in enumerate(p):
    result += (i+1) * j
print(result)