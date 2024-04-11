a = [5, 4, 3, 2, 1]
for i in range(0, len(a)):
    for j in range(i+1, len(a)):
        if a[j] < a[i]:
            a[i], a[j] = a[j], a[i]
print(a)
