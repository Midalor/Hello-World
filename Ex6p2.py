a=list(map(int, input("Введите значения через пробел: ").split()))
a.insert(0, a.pop())
print(*a)