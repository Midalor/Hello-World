a=set()

for i in input("Введите числа: ").split():

    if i not in a:

        a.add(i)

        print("NO")
    else:
        print("YES")