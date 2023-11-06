n=int(input("Введите количество элементов списка "))
spisok = list(map(int, input("Введиите значения: ").split()))[:n]
e=set(spisok)
print(len(e))