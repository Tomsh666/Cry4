import pandas as pd
def mul_table():
# Определяем элементы группы S_3
    elements = ['e', '(12)', '(13)', '(23)', '(123)', '(132)']

    # Создаем пустой DataFrame для таблицы умножения
    table = pd.DataFrame(index=elements, columns=elements)

    # Заполняем таблицу умножения
    for element1 in elements:
        for element2 in elements:
            # Выполняем умножение элементов element1 и element2
            result = ' '.join([element1, element2])
            # Обновляем соответствующую ячейку в таблице
            table.loc[element1, element2] = result
    # Выводим таблицу умножения
    print(table)

mul_table()
