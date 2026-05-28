a = [1,1,1,2,2,3]

officer = 0
res = 1

cm = 1
n = len(a)

while cm < n:

    if a[cm] == a[cm - 1]:
        cm += 1

    else:
        a[officer + 1] = a[cm]
        officer += 1
        res += 1
        cm += 1

print("Unique elements count:", res)

print("Array after removing duplicates:")
print(a[:res])