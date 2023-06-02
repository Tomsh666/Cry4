import pandas as pd
import group_elems
def mul_table(elements):
    # Создаем пустой DataFrame для таблицы умножения
    table = pd.DataFrame(index=elements, columns=elements)

    # Заполняем таблицу умножения
    for element1 in elements:
        for element2 in elements:
            # Выполняем умножение элементов element1 и element2
            result = ''.join(sorted(set(element1) & set(element2), key=element1.index))
            # Обновляем соответствующую ячейку в таблице
            table.loc[element1, element2] = result
    # Выводим таблицу умножения
    print(table)



#print(n=)
#n=int(input())
n=3
elems=group_elems.get_group_elements(n)
print('Элементы S_{l}'.format(l=n),elems)
print('Таблица умножения элементов S_{l}:'.format(l=n))
mul_table(elems)
