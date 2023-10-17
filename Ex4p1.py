n=int(input("Сколько вы хотите проверить чисел?: "))
k=0
for i in range(n):
   l=int(input())
   if(l==0):
       k+=1
print("количество нулей:", k)
