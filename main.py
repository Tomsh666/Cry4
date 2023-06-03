import pandas as pd
import group_elems
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
            result = compose(element1,element2)
            # Обновляем соответствующую ячейку в таблице
            table.loc[element1, element2] = result
    # Выводим таблицу умножения
    print(table)


#ввод
#print(n=)
#n=int(input())
n=4

#начало проги
elems=get_group_elements(n)
print('Элементы S_{l}'.format(l=n),elems)
print('Таблица умножения элементов S_{l}:'.format(l=n))
mul_table(elems)
