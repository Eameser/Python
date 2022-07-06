class Automobile:
    def __init__(self, code, mark, model, producting_year, type_of_carcass, price):
        self.code = code
        self.mark = mark
        self.model = model
        self.producting_year = producting_year
        self.type_of_carcass = type_of_carcass
        self.price = price

    def show_info(self):
        print("|%-5s|%-10s|%-20s|%-15s|%-15s|%-5s|" % (self.code, self.mark, self.model, str(self.producting_year), self.type_of_carcass, self.price))

auto = [Automobile(1, "chevrolet", "corvette", "1967", "sidan", 10000),
Automobile(2, "lada", "largus", "2014", "universal", 7000),
Automobile(3, "Shcoda", "octavia", "2014", "liftback", 7000)]

while True:
    try:
        x = int(input("==========================\n"
                      "1. Добавление информации.\n"
                      "2. Удаление информации.\n"
                      "3. Отображение информации.\n"
                      "4. Поиск по гожу выпуска.\n"
                      "Для выхода введите 0.\n"
                      "Введите номер задания: "))
    except:
        print("Ошибка, введен не верный номер задания. Попробуйте снова.")
        continue
    break

while x != 0:
    if x == 1:
        while True:
            try:
                code = int(input("Введите код авто: "))
            except:
                print("Ошибка. Попробуйте снова.")
                continue
            break
        mark = input("Введите макру авто: ")
        model = input("Введите модель авто: ")
        producting_year = input("Введите год выпуска авто: ")
        type_of_carcass = input("Введите тип кузова авто: ")
        while True:
            try:
                price = int(input("Введите цену авто: "))
            except:
                print("Ошибка. Попробуйте снова.")
                continue
            break
        if (price > 0):
            auto.append(Automobile(code, mark, model, producting_year, type_of_carcass, price))
        else:
            auto.append(Automobile(code, mark, model, producting_year, type_of_carcass, 2000))
               
    elif x == 2:
        while True:
            try:
                y = int(input("Номер для удаления: "))
            except:
                print("Ошибка. Попробуйте снова.")
                continue
            break
        for i in range(len(auto)):
            if(i == y):
                auto.pop(i)
    elif x == 3:
         print("|%-5s|%-10s|%-20s|%-15s|%-15s|%-5s|" % ("code", "mark", "model", "producting_year", "type_of_carcass", "price"))
         for i in range(len(auto)):
             auto[i].show_info()
    elif x == 4:
        while True:
            try:
                y = (input("Год выпуска авто: "))
            except:
                print("Ошибка. Попробуйте снова.")
                continue
            break
        q = False
        for i in range(len(auto)):
            if(auto[i].producting_year == y):
                q = True
                auto[i].show_info()
        if not(q):
            print("Автомобилей с таким годом выпуска нет. Попробуйте снова.")
    else: print("Ошибка, введен не верный номер задания. Попробуйте снова.")

    while True:
        try:
            x = int(input("==========================\n"
                      "1. Добавление информации.\n"
                      "2. Удаление информации.\n"
                      "3. Отображение информации.\n"
                      "4. Поиск по году выпуска.\n"
                      "Для выхода введите 0.\n"
                      "Введите номер задания: "))
        except:
            print("Ошибка, введен не верный номер задания. Попробуйте снова.")
            continue
        break

    







