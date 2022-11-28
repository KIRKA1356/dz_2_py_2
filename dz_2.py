# # Задача 1
# def del_2_and_3():
#     """ 
#         Функция показывает кол-во чисел делящихся и на 2 и  на 3 и показывает эти числа списком
#     """
#     num_x = int(input("Введите число X: "))
#     num_y = int(input("Введите число Y: "))
#     max = 0
#     min = 0
#     result = 0
#     if num_x>num_y: 
#         max = num_x
#         min = num_y
#     else:
#         max = num_y
#         min = num_x
#     list_num=[]
#     for i in range(min, max+1):
#         if i%2==0 and i%3==0:
#             result=result + 1
#             list_num.append(i)
    
#     print(f"Кол-во:", result)
#     print(f"Числа подходящие под ваши параметры:", list_num)


# del_2_and_3()

# Задача 2
# def max_of_number():
#     num_x = int(input("Введите кол-во чисел которое будете вводить: "))
#     list_num  = []
#     for i in range (0,num_x):
#         num_y = int(input("Введите число: "))
#         list_num.append(num_y)

#     max_full = 0
#     max_2_full = 0
#     for i in list_num:
#         if i > max_full: 
#             max_2_full = max_full
#             max_full = i

#         elif i>max_2_full: 
#             max_2_full = i

#     print(f'Вы ввели:', list_num)
#     print(f'Максимальное число:',max_full,'Второе поссле максимума число:', max_2_full)
# max_of_number()

# Задача 3
# def max_of_number():
#     zap = int(input("Введите заработную плату: "))
#     rub_25 = 0
#     rub_10 = 0
#     rub_3 = 0
    
    
#     if (zap%25==0):
#         rub_25 = int(zap / 25)
#         ost = 0
#     elif(zap>25):
#         rub_25 = int(zap / 25)
#         ost = zap - rub_25 * 25
#     if (ost%10==0 and ost!=0):
#         rub_10 = int(ost / 10)
#         ost = 0
#     elif(zap>10):
#         rub_10 = int(ost / 10)
#         ost = ost - rub_10 * 10
#     if (ost%3==0 and ost!=0):
#         rub_3 = int(ost / 3)
#         ost = 0
#     elif(zap>13):
#         rub_3 = int(ost / 3)
#         ost = ost - rub_3 * 3
#     print(f'Купюр номиналом 25:',rub_25)
#     print(f'Купюр номиналом 10:', rub_10)
#     print(f'Купюр номиналом 3:',rub_3)
#     print(f'Купюр номиналом 1:',ost)
# max_of_number()

# Задача 4

# def order():
#     num = (input("Введите число: "))
#     bad = sorted(num)
#     list = []
#     for i in num:
#         list.append(i)
#     if list == bad: print("Упорядочено")
#     else:print("Неупорядочено") 
# order()            
