def solution(num):                              # Функция считающая всё
    odin = num%1000%100%10                      # Считает кол-во единиц
    des = num%1000%100//10                      # Считает кол-во десятков
    sot = num%1000//100                         # Считает кол-во сотен
    tus = num//1000                             # Считает кол-во тысяч
    #print(tus,sot,des,odin)

    listodin = [0,1,2,3,4,5,6,7,8,9]            # Список чисел, которые будут перебраны
    listodin2 = ['','I','II','III','IV','V','VI','VII','VIII','IX'] # Список Римских чисел, который будет перебран
    for i in listodin:                          # Цикл перебирающий список чисел
        for k in listodin2:                     # Цикл перебирающий список Римских чисел
            if odin == i:                       # Если "единица" равна числу из первого списка, то
                r = listodin2[i]                # переменная r принимает значение из второго списка по индексу числа

    listdes = [0,1,2,3,4,5,6,7,8,9]             # Список чисел, которые будут перебраны
    listdes2 = ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']  # Список Римских чисел, который будет перебран
    for i_1 in listdes:                         # Цикл перебирающий список чисел
        for k_1 in listdes2:                    # Цикл перебирающий список Римских чисел
            if des == i_1:                      # Если "Десяток" равен числу из первого списка, то переменная
                r2 = listdes2[i_1] + r          # r2 принимает значение из второго списка по индексу числа и прибавляет
                #print(r2)                      # прошлую переменную

    listsot = [0,1,2,3,4,5,6,7,8,9]             # Список чисел, которые будут перебраны
    listsot2 = ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']  # Список Римских чисел, который будет перебран
    for j in listsot:                           # Цикл перебирающий список чисел
        for n in listsot2:                      # Цикл перебирающий список Римских чисел
            if sot == j:                        # Если "Сотня" равна числу из первого списка, то
                r3 = listsot2[j] + r2           # переменная r3 принимает значение из второго списка по индексу числа и
                                                # прибавляет прошлую переменную

    listtus = [0,1,2,3]     # Список чисел, которые будут перебраны
    listtus2 = ['','M','MM','MMM']  # Список Римских чисел, который будет перебран
    for j_1 in listtus:                         # Цикл перебирающий список чисел
        for n_1 in listtus2:                    # Цикл перебирающий список Римских чисел
            if tus == j_1:                      # Если "Тысяча" равна числу из первого списка, то возвращает
                # значение из второго списка по индексу числа и прибавляет прошлую переменную
                return listtus2[j_1] + r3

solution(1000)                                  # Число которое надо перевести в Римское