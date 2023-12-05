def f(i): return 1 if i == 1 else i * f(i - 1) 
n = int(input("Введите значение: ")) 
f1 = f(n)
print(f1)
spisok = [f(f1 - i) for i in range(f1)] 
print(spisok)

