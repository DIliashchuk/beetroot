# вивести ОДИН раз всі числа якщо вони закінчуються на одну і ту ж цифру
# вивести ОДИН раз всі числа якщо вони націло діляться на 4

a = 0
b = 0
c = 0
done_end_with_the_same_number = False
done_devide_by_4 = False
while True:
    a += 1
    b += 2
    c += 3
    if str(a)[-1] == str(b)[-1] == str(c)[-1]:
        print(a, b, c)
        done_end_with_the_same_number = True

    if a % 4 == 0 and b % 4 == 0 and c % 4 == 0:
        print(a, b, c)
        done_devide_by_4 = True

    if done_end_with_the_same_number and done_devide_by_4:
        break