def recursive_print(lst):
    if len(lst) == 0:
        print("Конец списка")
        return
    else:
        print(lst[0])
        recursive_print(lst[1:])

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
ff = list(reversed(my_list))
recursive_print(ff)