import math

while True:
    ex = int(input("Введите номер задания: "))

    if(ex == 1):
        while True:
            try:
                a = int(input("Введите a: "))
                n = int(input("Введите n: "))
                m = int(input("Введите m: "))
                break
            except ValueError:
                print("Ошибка! Введите число.")
        form1 = int((abs(math.cos(a)) ** n) ** m)
        form2 = int((math.exp(n ** 3)) / (math.log(a)))
        form3 = int(pow((math.sin(a ** 2)), 1/n).real)

        print(form1 + form2 + form3)

    elif(ex == 2):
        # y = (input("1 - показать значения списка на экране; \n 2 - добавление нового элементов в конец списка (добавлять элементы разных типов); \n 3 - удаление указанного пользователем элемента из списка; \n 4 - сформировать кортеж из нечетных позиций списка и вывести его на экран; \n 5 - найти произведение всех вещественных элементов списка; \n 6 - сформировать строку из значений элементов списка и посчитать количество знаков препинания в строке; \n 7 - задать с клавиатуры множество M1, сформировать множество M2 из списка; вывести на экран множество, полученное путем пересечения множеств M1 и M2; \n 8 - получить из списка словарь, ключом каждого элемента сделать позицию элемента в словаре; построчно отобразить на экране элементы словаря с ключом меньше 5; \n 9 - Выход. \n "))
        while True:
            try:
                ex2 = int(input("--------------------------\n"
                               "Задание №2.\n"
                               "1. показать значения списка на экране.\n"
                               "2. добавить новый элемент в конец списка.\n"
                               "3. удалить указанный элемент.\n"
                               "4. сформировать кортеж из нечетных позиций списка и вывести его на экран.\n Вывести содержимое кортежа на экран.\n"
                               "5. найти произведение всех вещественных элементов списка.\n"
                               "6. сформировать строку из значений элементов списка и посчитать количество знаков препинания в строке.\n"
                               "7. задать с клавиатуры множество M1, сформировать множество M2 из списка.\n Вывести на экран множество, полученное путем пересечения множеств M1 и M2.\n"
                               "8. получить  из  списка  словарь,  ключом  каждого  элемента  сделать  позицию  элемента  в словаре.\n  Построчно  отобразить  на  экране  элементы словаря с ключом меньше 5.\n"                             
                               "9. ВЫХОД.\n"
                               "Введите номер подзадания:"))
            except:
                print("Ошибка, введен не верный номер задания. Попробуйте снова.")
                continue
            break
        a = [3, -12, 'Michael', 2.0]
        while ex2 != 0:
            if ex2 == 1:
                print(a)
            elif ex2 == 2:
                t = (input("Введите тип: "))
                if (t == "str"):
                    while True:
                        try:
                            x = (input("Ввведите значение: "))
                        except:
                            print("Ошибка. Попробуйте снова.")
                            continue
                        break
                    a.append(x)
                elif (t == "int"):
                    while True:
                        try:
                            x = int(input("Ввведите значение: "))
                        except:
                            print("Ошибка, введено не целое число. Попробуйте снова.")
                            continue
                        break
                    a.append(x)
                elif (t == "float"):
                    while True:
                        try:
                            x = float(input("Ввведите значение: "))
                        except:
                            print("Ошибка, введено значение не типа float. Попробуйте снова.")
                            continue
                        break
                    a.append(x)
            elif ex2 == 3:
                while True:
                        try:
                            x = int(input("Ввведите номер: "))
                        except:
                            print("Ошибка, введено не целое число. Попробуйте снова.")
                            continue
                        break
                try:
                    a.pop(x)
                except:
                    print("Ошибка, элемента с данным номером не существует.")       
            elif ex2 == 4:
                b = []
                for i in a:
                   #if isinstance(i,int):
                       if (a.index(i) % 2) != 0:
                             b.append(i)
                print("Кортеж: ")
                print(tuple(b))
            elif ex2 == 5:
                p = float(1)
                for i in a:
                    if isinstance(i,float):
                       p = float(p) * i
                print("Произведение: " + str(p))
            elif ex2 == 6:
                sum = 0
                list2 = []
                test = ['.', ',']
                for i in a:
                    list2.append(str(i))
                str1 = ', '.join(list2)
                for obj in str1:
                    if obj in test:
                        sum += 1
                print("Колличество знаков перпинания: ", sum)
            elif ex2 == 7:
                b = {i for i in range(10)}
                print(set(a))
                print(b)
               # z ={}
               # z = a.inrsection(b) 
                print("Пересечение множеств: ")
                print(set(a) & b)
            elif ex2 == 8:
                d = { }
                for i in range(len(a)):
                    d[i] = a[i]
                print("Словарь: ")
                print(d)
                for i in range(len(a)):
                   if i < 5:
                       print("Элемент " + str(i) + ": " +str(d[i]))
            else:
                print("Ошибка, введен не верный номер задания. Попробуйте снова.")
            while True:
                try:
                    ex2 = int(input("--------------------------\n"
                               "Задание №2.\n"
                               "1. Показать значения списка на экране.\n"
                               "2. Добавить новый элемент в конец списка.\n"
                               "3. Удалить указанный элемент.\n"
                               "4. Сформировать кортеж, состоящий из вещественных положительных элементов списка.\n Вывести содержимое кортежа на экран.\n"
                               "5. Найти произведение всех целочисленных элементов списка.\n"
                               "6. Сформировать  строку  из  значений  элементов  списка.\n  Посчитать  сколько  раз встречается в строке указанное пользователем слово.\n"
                               "7. Задать с клавиатуры множество M1, сформировать множество M2 из списка.\n Вывести на экран симметричную разницумножеств M1 и M2.\n"
                               "8. Получить  из  списка  словарь,  ключом  каждого  элемента  сделать  позицию  элемента  в словаре.\n  Построчно  отобразить  на  экране  элементы  словаря  с  нечетными  значениями ключа.\n"                             
                               "Для выхода введите 0.\n"
                               "Введите номер подзадания: "))
                except:
                    print("Ошибка, введен не верный номер задания. Попробуйте снова.")
                    continue
                break


    elif(ex == 3):
        x = (input("Площадь чего вы хотите посчитать? \n T - площадь трапеции \n R - площадь ромба \n E - площадь равностороннего треугольника \n Q - Выход из программы \n "))
        # print("T - площать трапеции")
        while True:
            if(x == "T"):
                # print("t")
                a = int(input("Введите первое основание a: "))
                b = int(input("Введите первое основание b: "))
                h = int(input("Введите высоту h: "))
                S = ((a + b)/2) * h
                print("Площадь трапеции = ", S)
                break

            elif(x == "R"):
                a = int(input("Введите диагональ a: "))
                b = int(input("Введите диагональ b: "))
                S = (a * b)/2
                print("Площадь ромба = ", S)
                break

            elif(x == "E"):
                a = int(input("Введите сторону a: "))
                S = (a **2 * 3 ** 1/2) / 4
                print("Площадь равностороннего треугольника = ", S)
                break

            elif(x == "Q"):
                break

    