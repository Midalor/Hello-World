a= int(input("Введите число: "))
n=a
m=a
spisok=[]
while n > 1:
    n=n-1
    m*=n
for lenght in range(m, 1, -1):
    i=lenght
    y=lenght
    while y > 1:
        y=y-1
        i*=y
    spisok.append(i)
spisok.append(y)
print(spisok)
    