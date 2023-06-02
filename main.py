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

def mul_table(elements):
    # Создаем пустой DataFrame для таблицы умножения
    table = pd.DataFrame(index=elements, columns=elements)

    # Заполняем таблицу умножения
    for element1 in elements:
        for element2 in elements:
            # Выполняем умножение элементов element1 и element2
            result = eval(element1+element2)
            # Обновляем соответствующую ячейку в таблице
            table.loc[element1, element2] = result
    # Выводим таблицу умножения
    print(table)


#ввод
#print(n=)
#n=int(input())
n=3

#начало проги
elems=get_group_elements(n)
print('Элементы S_{l}'.format(l=n),elems)
print('Таблица умножения элементов S_{l}:'.format(l=n))
mul_table(elems)
