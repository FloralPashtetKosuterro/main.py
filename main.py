
chislo = int(input("Введите число больше нуля: "))
stroka = input("Введите слово, которое заменит чётное число: ")
spisok = list(range(1, chislo + 1))

for g in range(len(spisok)):
    if spisok[g] % 2 == 0:
        spisok[g] = stroka
print(spisok)