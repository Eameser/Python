import math

a, n, m = map(int, input("Задание №1.\nВведите a, n и m: ").split())
f = lambda a, n, m: print("Ответ: ", ((abs(math.cos(a)) ** n) ** m + (math.exp(n ** 3)) / (math.log(a)) + pow((math.sin(a ** 2)), 1/n).real))
f(a,n,m)

A = [['T', 'R', 'E', 'Q', 'T'],[2,3,6]] 
Trapezoid = lambda a,b,h: (int(a)>0 and int(b)>0 and int(h)>0 and 0.5 * (int(a) + int(b)) * int(h)) or print("Ошибка, попробуйте снова.")
Rhombus = lambda a, b: (int(a)>0 and int(b)>0 and 0.5 * int(a) * int(b)) or print("Ошибка, попробуйте снова.")
Equilateral_triangle = lambda a: (int(a)>0 and 0.25 * int(a) **2 * 3 ** 1/2) or print("Ошибка, попробуйте снова.")
exit = lambda : 0
f = list(map(str,A[0]))
d = list(map(str,A[1]))
choice = lambda : list(map(lambda a:(a =='T') and Trapezoid(d[0], d[1], d[2]) or (a =='R') and Rhombus(d[0], d[1]) or (a =='E') and Equilateral_triangle (d[0]) or  (a =='Q') and exit(),f ))
print("Задание №2\nОтвет:")
print(choice())