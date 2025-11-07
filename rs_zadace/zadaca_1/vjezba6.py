print("1. ----------")

sum_even = 0
for i in range(1, 101):
    if i % 2 == 0:
        sum_even += i
print(sum_even)

sum_even = 0
i = 1
while i <= 101:
    if i % 2 == 0:
        sum_even += i
    i += 1
print(sum_even)

print("2. ----------")

for i in range(19, 0, -2):
    print(i)

i = 19
while i >= 1:
    print(i)
    i -= 2

print("3. ----------")

a, b = 0, 1
while a <= 1000:
    print(a)
    a, b = b, a + b

a, b = 0, 1
for _ in range(1000):
    if a > 1000:
        break
    print(a)
    a, b = b, a + b
