a = []
n = int(input("Введите количество значений:"))
for i in range(n):
    a.append(int(input("Введите значение: ")))
a.reverse()
print(*a)