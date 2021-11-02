from random import *
inimesed = ["A", "B"]
palgad = [2000,2000]
N = 4
def sisesta_andmed(i,p):
    for n in range(N):
        inimene = input("Введите имя: ")
        i.append(inimene)
        palk = randint(100,10000)
        p.append(palk)
    return i,p
def andmed_ekranile(i,p):
    N=len(i)
    for n in range(N):
        print(i[n],"-",p[n])
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
                print(t,".",i[e],"-",p[e])
        j=int(input("Порядковый номер человека: "))
        i.pop(abi_list[j-1])
        p.pop(abi_list[j-1])
        andmed_ekranile(i,p)
    return i,p
def sorteerimine(i,p,v):
    N=len(p)
    if v==1:
        for n in range(0,N):
            for m in range(n,N):
                if p[n]<p[m]:
                    abi=p[n]
                    p[n]=p[m]
                    p[m]=abi
                    abi=i[n]
                    i[n]=i[m]
                    i[m]=abi
    else:
         for n in range(0,N):
            for m in range(n,N):
                if p[n]>p[m]:
                    abi=p[n]
                    p[n]=p[m]
                    p[m]=abi
                    abi=i[n]
                    i[n]=i[m]
                    i[m]=abi

    andmed_ekranile(i,p)
def vordsed_palgad(i,p):
    N=len(p)
    dublikatid=[x for x in palgad if palgad.count(x)>1]
    print(list(set(dublikatid)))
while 1:
    valik=input("a - Ввод данных\ne -Показать данные \nk - Удаление\ns- Сортировка\nv - Проверка одинаковой зарплат\n")
    if valik.lower()=="a":
        inimesed,palgad=sisesta_andmed(inimesed,palgad)
    elif valik.lower()=="e":
        andmed_ekranile(inimesed,palgad)
    elif valik=="k":
        inimesed,palgad=kustutamine(inimesed,palgad)
    elif valik.lower()=="s":
        sorteerimine(inimesed,palgad,int(input("1 - Сортировка по убыванию.\n2 - Сортировка по возрастанию.\n")))
    elif valik.lower()=="v":
        vordsed_palgad(inimesed,palgad)
    else:
        break
