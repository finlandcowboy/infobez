import random

#! Функция возвращающая (x^y) % p
def power(x, y, p):
	#* Инициализируем переменную результат равную 1, т.к.
    #TODO: добавить почему
	res = 1

	#* Если x больше чем p, то обновляем значение x до остатка от деления от p
	x = x % p
	while (y > 0):

	        #* Если y нечетный - домножаем результат на x и берем остаток от деления на p
		if y & 1:
			res = (res * x) % p

		#* теперь y - четный
		y = y >> 1
		x = (x * x) % p

	return res

#! Тест Миллера
#? Вызывается k раз
#? Возвращает True, если число предположительно простое. False если составное
def millerTest(d, n):

    #* Выбирается рандомное значение в отрезке [2;n-2] (Очевидно, n > 4)
	a = 2 + random.randint(1, n - 4)

	#* Вычисляем a^d % n
	x = power(a, d, n)

	if (x == 1 or x == n - 1):
		return True

	while (d != n - 1):
		x = (x * x) % n
		d *= 2

		if (x == 1):
			return False
		if (x == n - 1):
			return True

	return False

#* К - значение количества раз, которое будет вызыватся тест Миллера, чем больше, тем выше точность
def isPrime(n, k):

	#* Краевой случай
	if (n <= 1 or n == 4):
		return False
	if (n <= 3):
		return True

    #* Находим такое число r, что n = 2^d * r + 1 (где r >=1)
	d = n - 1
	while (d % 2 == 0):
		d //= 2

	#* Выполняем тест Миллера k раз
	for i in range(k):
		if (millerTest(d, n) == False):
			return False

	return True

# number = int(input('Введите число: '))
# k = int(input('Введите количество итерация теста Миллера. Рекомендованное значение: 40\nЗначение:'))

# print(isPrime(number,k))


# print("All primes smaller than 100: ")
# for n in range(1, 1000):
# 	if (isPrime(n, k)):
# 		print(n, end=" ")

# # This code is contributed by mits
