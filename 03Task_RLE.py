# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
def rle_encode(data):

    encoding = ""  # сохраняет выходную строку

    i = 0
    while i < len(data):
        # подсчитывает количество вхождений символа в индексе `i`
        count = 1

        while i + 1 < len(data) and data[i] == data[i + 1]:
            count = count + 1
            i = i + 1

        # добавляет к результату текущий символ и его количество
        encoding += str(count) + data[i]
        i = i + 1

    return encoding


def rle_decode(data):  # декодирование
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode


s = 'ABBCCCD'
# print(rle_encode(s))
zashifr = rle_encode(s)
print('Зашифровали  ', zashifr)
rasshifr = rle_decode(zashifr)
print('Расшифровали ', rasshifr)
