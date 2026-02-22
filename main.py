# 1
n = int(input())
s = 0
for i in range(1, n + 1):
    s += i
print(s)

# 2
n = int(input())
s = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        s += i
print(s)

# 3
n = int(input())
s = 0
for i in range(1, n + 1):
    if i % 2 != 0:
        s += i
print(s)

# 4
n = int(input())
p = 1
for i in range(1, n + 1):
    p *= i
print(p)

# 5
n = int(input())
count = 0
for i in range(1, n + 1):
    count += 1
print(count)
