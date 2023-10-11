number = int(input("Введите 5-ти значное число:"))
ones = number % 10
tens = (number // 10) % 10
hundreds = (number // 100) % 10
thousands = (number // 1000) % 10
tens_of_thousands = (number // 10000) % 10

result = ((tens ** ones)*hundreds)/(tens_of_thousands-thousands)
print(result)

