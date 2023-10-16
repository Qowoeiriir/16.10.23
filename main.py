 # №2
l = [64, 25, 12, 22, 11, 1,2,44,3,122, 23, 34]

for i in range(len(l)):
    for j in range(i + 1, len(l)):

        if l[i] > l[j]:
            l[i], l[j] = l[j], l[i]

 print (l)

# №3
 # Функция нахождения значения максимально приближённого к лимиту, но не привышающее его
 def lim_max(nums_, limit_):
     # В эту переменную вносятся значения которые меньше лимита
     summ = 0

     # Цикл который проверяет значения элементов кортежа
     for i in range(0, len(nums_)):

         # Если условие выполняется то в переменную summ вносится значение текущего элемента
         if nums_[i] < limit_:
             summ = nums_[i]

     # Возвращаем переменную с её значением
     return summ


 # заранее подготовленный кортеж
 nums = (10, 20, 30, 40, 50, 60, 70, 80, 100)

 # вводим лимит
 limit = int(input('Введите лимит: '))

 # Выводим возвращаемое функцией значение
 print(lim_max(nums, limit))
 ''
 def lin_max(nums, limit):
     max_0 = -1
     for i in nums:
         if i < limit and i > max_0:
             max_e = i
     nums = (10, 20, 30, 40, 50, 60, 70, 80, 100)
     limit = 40
     moodl = lim_max(nums, limit)
     print(moodl)

 # №4
 def temp_cat(temp):
     if temp < -20:
         return 0
     elif -20 < temp < 0:
         return 1
     elif 0 < temp < 15:
         return 2
     elif 15 < temp < 25:
         return 3
     elif temp > 25:
         return 4
 temp = 12
 pip = temp_cat(temp):
 print(pip)



