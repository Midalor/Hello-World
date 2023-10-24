a = []
b = []
n = int(input("Введите количество рыбаков:"))
m = int(input("Введите максимальную массу которую может выдержать лодка:"))
for AI in range(n):
    a.append(int(input("Введите вес каждого путешественника:")))
for x in range(len(a)):
    if a[x] + min(a) <= m:
        b += [[a[x], min(a)]]
        a[x] += m
        a[a.index(min(a))] += m
    else:
        if a[x] > m:
            continue
        else:
            b += [[a[x]]]
print(len(b))