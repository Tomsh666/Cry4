import pandas as pd
import math
import itertools

def get_group_elements(n):
    elements = []
    # Генерация всех возможных перестановок длиной n
    permutations = list(itertools.permutations(range(1, n + 1)))

    # Преобразование перестановок в строковое представление
    for perm in permutations:
        perm_str = "".join(str(p) for p in perm)
        #elements.append(int(perm_str))
        elements.append(perm_str)
    return elements

def strtoarr(a):
    a = list(a)
    for i in range(0,len(a)):
        a[i]=int(a[i])
    return a

def compose(a,b):
    a = strtoarr(a)
    b = strtoarr(b)
    rez=[]
    for i in range(0,len(a)):
        #умножение
        #print(i,'->',b[i],'->',a[b[i]-1])
        rez.append(a[b[i]-1])
    return rez


def mul_table(elements):
    # Создаем пустой DataFrame для таблицы умножения
    table = pd.DataFrame(index=elements, columns=elements)

    # Заполняем таблицу умножения
    for element1 in elements:
        for element2 in elements:
            # Выполняем умножение элементов element1 и element2
            res = compose(element1,element2)
            result=''
            for i in res:
                result+=str(i)
            # Обновляем соответствующую ячейку в таблице
            table.loc[element1, element2] = result
    # Выводим таблицу умножения
    print(table)
    return table

def mul(table,elem1,elem2):
    return table.at[elem1,elem2]

def subgroups(table,n):
    narr=[]
    for i in range(1,math.factorial(n)+1):
        if math.factorial(n)%i==0:
            narr.append(i)
    for i in range(0,math.factorial(n)):
        gr=table.index[i]
        resarr=[]
        resarr.append(gr)
        po = 1
        while gr!='123' and po<=math.factorial(n):
            gr=mul(table,gr,gr)
            resarr.append(gr)
            po+=1
        if po in narr:
            #print(resarr)
            rightarr = []
            leftarr = []
            for t in range(0,math.factorial(n)):
                for j in resarr:
                    rightarr.append(mul(table,j,table.index[t]))
                    leftarr.append(mul(table,table.index[t],j))
                if rightarr==leftarr:
                    print(resarr)
                    break
                rightarr.clear()
                leftarr.clear()



    #print(narr)


#ввод
#print(n=)
#n=int(input())
n=3

#начало проги
elems=get_group_elements(n)
print('Элементы S_{l}'.format(l=n),elems)
print('Таблица умножения элементов S_{l}:'.format(l=n))
table=mul_table(elems)
subgroups(table,n)