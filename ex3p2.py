glasn= ['a','e','i','u','y','o']
sogl= ['q','w','r','t','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
word= input("Введите слово: ")
x=0
z=0
y=0
for g in glasn:
    for letter in word:
        if letter == g:
            x+=1
    if x == 0:
            print(g, ":False")
    else:
        print(g, ":", x)
    y+=x
    x=0
for s in sogl:
    for letter in word:
        if letter == s:
            z+=1
print("Согласных: ", z)
y+=z
print("Всего Букв:", y)
