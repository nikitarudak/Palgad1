from random import *
inimesed = ["A", "B","A","D"]
palgad = [2000,150,2000,300,]

def sisesta_andmed(i,p):
    N = int(input("Введите кол-во людей: "))
    for n in range(N):
        inimene = input("Введите имя: ")
        i.append(inimene)
        palk = randint(100,10000)
        p.append(palk)
    return i,p
def andmed_ekranile(i,p):
    N=len(i)
    for n in range(N):
        print(f"{i[n]} - {p[n]}")
def kustutamine(i,p):
    nimi=input("Введите имя человека, которого нужно удалить: ")
    n=i.count(nimi)
    abi_list=[]
    if n > 0:
        t=0
        for e in range(len(i)):
            if i[e]==nimi:
                t+=1
                abi_list.append(int(e))
                print(f"{t}.{i[e]} - {p[e]}")
        j=int(input("Порядковый номер человека: "))
        i.pop(abi_list[j-1])
        p.pop(abi_list[j-1])
        andmed_ekranile(i,p)
    return i,p
def sorteerimine(i,p,v):
    """Sorteerimine palgade järgi.

    Tagastame inimeste ja palgade listid teise funktsiooni kasutamisel

    :param list 1: Inimeste järjend.
    :param list p: Palgade järjend.
    :param int v: sorteerimise tüüp
    :rtype: list,list
    """
    N = len(p)
    if v == 1:
        for n in range (0, N):
            for m in range (n, N):
                if p[n]<p[m]:
                    abi=p[n]
                    p[n]=p[m]
                    p[m]=abi
                    abi=i[n]
                    i[n]=i[m]
                    i[m]=abi
    else:
        for n in range (0, N):
            for m in range (n, N):
                if p[n]>p[m]:
                    abi=p[n]
                    p[n]=p[m]
                    p[m]=abi
                    abi=i[n]
                    i[n]=i[m]
                    i[m]=abi

    andmed_ekranile(i ,p)
def sort_nimi_jargi(p,i):
    N = len(p)
    k = int(input("1 - сортировать А -> Я\n2 - сортировать Я -> А\n "))
    if k == 1:
        for n in range (0, N):
            for m in range (n, N):
                if p[n]<p[m]:
                    abi=p[n]
                    p[n]=p[m]
                    p[m]=abi
                    abi=i[n]
                    i[n]=i[m]
                    i[m]=abi
    else:
        for n in range (0, N):
            for m in range (n, N):
                if p[n]>p[m]:
                    abi=p[n]
                    p[n]=p[m]
                    p[m]=abi
                    abi=i[n]
                    i[n]=i[m]
                    i[m]=abi

    andmed_ekranile(i ,p)
def vordsed_palgad(i, p):
    N = len(p)
    dublikatid = [ x for x in palgad if palgad.count(x)>1 ]
    dublikatid = list(set(dublikatid))
    for palk in dublikatid:
        n = p.count(palk)
        k = -1
        for j in range(n):
            k = p.index(palk, k+1)
            nimi = i[k]
            print(f"{nimi} получает {palk}")
def maximum(palk,inimesed):
    max_palk = palk[0]
    nimi = inimesed[0]
    for p in palk:
        if p > max_palk:
            max_palk = p
            i = palk.index(max_palk)
            nimi = inimesed[i]
    print(f"Максимальную зарплату {max_palk} получает {nimi}")   
def minimum(palk,inimesed):
    min_palk = palk[0]
    nimi = inimesed[0]
    for p in palk:
        if p < min_palk:
            min_palk = p
            i = palk.index(min_palk)
            nimi = inimesed[i]
    print(f"Минимальную зарплату {min_palk} получает {nimi}")
def nimi(i, p):
    otsi_nimi = []
    otsi_palk = []
    palk_keda = 0
    keda = input("Введите имя: ")
    n = len(inimesed)
    for j in range(n):
        if inimesed[j] == keda:
            palk_keda = palgad[j]
            otsi_nimi.append(inimesed[j])
            otsi_palk.append(palk_keda)
        else:pass
    for i in range(len(otsi_nimi)):
        print(f"{otsi_nimi[i]} - {otsi_palk[i]}")
def kesk1(palk):
    summa = 0
    n = len(palk)
    for p in palk:
        summa += p
    summa = summa/n
    print(f"Средняя зарплата равна {summa}")
def kesk(i, p):
    summa=0
    t=False
    for palk in p:
        summa+=palk
    summa/=len(p)
    print(f"Средняя зарплата: {summa}")
    for palk in p:
        if palk==summa:
            n=p.index(palk)
            print(f"Получает: {i[n]}")
            t=True

    if t!=True:   print("Такие люди отсутсвуют!")
def erinev_palk(i, p):
    number = int(input("Введите зарплату: "))
    tin = int(input("Больше или меньше зарплаты? 1 или 2: "))
    for i in palgad:
        if tin == 1:
            if i > number:
                ind = palgad.index(i)
                nimi = inimesed[ind]
                print(f"{nimi} - {i}")
        else:
            if i < number:
                ind = palgad.index(i)
                nimi = inimesed[ind]
                print(f"{nimi} - {i}")
def top(i, p):
    N = len(p)
    v = int(input("Богатые или бедные - 1/2: "))
    if v == 1:
        for n in range (0, N):
            for m in range (n, N):
                if p[n] < p[m]:
                    abi = p[n]
                    p[n] = p[m]
                    p[m] = abi
                    abi = i[n]
                    i[n] = i[m]
                    i[m] = abi
        k = 3
        print("Топ 3 богатых")
        for i in range(0, k, 1):
            print(f"{inimesed[i]} - {palgad[i]}")
    else:
        for n in range (0, N):
            for m in range (n, N):
                if p[n] > p[m]:
                    abi = p[n]
                    p[n] = p[m]
                    p[m] = abi
                    abi = i[n]
                    i[n] = i[m]
                    i[m] = abi
        k = 3
        print("Топ 3 бедных")
        for i in range(0, k, 1):
            print(f"{inimesed[i]} - {palgad[i]}")
def tulumaks(i, p):
    z = int(input("Введите зарплату: "))
    k = 0
    if z < 1200:
        t = (z-500)*0.2
        k = z - t
    elif z > 1200 <= 2100:
        t = 500-(500/850)*(z-1200)
        k = z - t
    else:
        k = z*0.2
    print(f"Нетто зарплата - {round(k,2)}")
def kustutamine_kesk(i, p):
    summa = 0
    for palk in palgad:
        summa+=palk
    summa/=len(palgad)
    n = len(palgad)
    for i in range(n):
        for palk in palgad:
            if palk < summa:
                g = int(palgad.index(palk))
                palgad.remove(palk)
                inimesed.pop(g)
    N=len(inimesed)
    for n in range(N):
        print(f"{inimesed[n]} - {palgad[n]}")

while 1:
    valik=input("\na - Ввод данных\ne - Показать данные \nk - Удаление\nkk - Удаление из списка людей, который получают меньше средней\ns1 - Сортировка по числам\ns2 - Сортировка по буквам\nv - Проверка одинаковых зарплат\nma - Максимальна зарплата\nmi - Минимальная зарплата\nnimi - Поиск зарплаты по имени\nkesk - Средняя зарплата\nh - Список людей, которые полчают >/< введеной зарплаты\ntop - Топ 3 богатых и бедных\ntul - Зарплата с вычетом налогов\n")
    if valik.lower() == "a":
        inimesed,palgad=sisesta_andmed(inimesed,palgad)
    elif valik.lower() == "e":
        andmed_ekranile(inimesed,palgad)
    elif valik.lower() == "k":
        inimesed,palgad=kustutamine(inimesed,palgad)
    elif valik.lower() == 'kk':
        kustutamine_kesk(inimesed, palgad)
    elif valik.lower() == "s1":
        sorteerimine(inimesed, palgad, int(input("1 - Сортировка по убыванию.\n2 - Сортировка по возростанию.\n")))
    elif valik.lower() == 's2':
        sort_nimi_jargi(inimesed, palgad)
    elif valik.lower() == "v":
        vordsed_palgad(inimesed, palgad)
    elif valik.lower() == 'max':
        maximum(inimesed, palgad)
    elif valik.lower() == 'min':
        minimum(inimesed, palgad)
    elif valik.lower() == 'nimi':
        nimi(inimesed, palgad)
    elif valik.lower() == 'kesk':
        kesk(inimesed, palgad)
    elif valik.lower() == 'h':
        erinev_palk(inimesed, palgad)
    elif valik.lower() == 'top':
        top(inimesed, palgad)
    elif valik.lower() == 'tul':
        tulumaks(inimesed, palgad)
    else:
        break