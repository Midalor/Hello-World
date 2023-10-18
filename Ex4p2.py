x = int(input("Введите число:"))
count = 0
for i in range(1, x+1):
    if x % i == 0:
        count += 1      
if count == 2:
    print("Число простое, колличество множителей", count)
else:
    print("Число не простое, колличество множителей", count)
