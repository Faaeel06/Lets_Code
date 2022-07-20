a = 0
n = int(input())
for i in range(n):
    for j in range(i + 1, n):
        a = a + 1
        a = a + j

print(a)

