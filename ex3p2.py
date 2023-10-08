vowels = 'aeiuy' 
word = (input("Введите слово: ")).lower() 
print('количество согласных', 
len(list(filter(lambda x: not x in vowels,word))))
print('количество гласных', len(list(filter(lambda x: x in vowels, word))))
