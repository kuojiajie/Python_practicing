def read_file(file_name):
    lines = []
    with open(file_name, 'r', encoding = 'utf-8-sig') as file:
        for line in file:
            lines.append(line.strip())
    return lines


def analytics(lines):
    Allen_word_count = 0
    Viki_word_count = 0
    Allen_sticker_count = 0
    Viki_sticker_count = 0
    Allen_image_count = 0
    Viki_image_count = 0
    for line in lines:
        cut_line = line.split(' ') #分割的文字以清單儲存
        time = cut_line[0]
        name = cut_line[1]
        if name == 'Allen':
            if cut_line[2] == '貼圖':
                Allen_sticker_count += 1
            elif cut_line[2] == '圖片':
                Allen_image_count += 1
            else:
                for msg in cut_line[2:]:
                    Allen_word_count += len(msg)
        elif name == 'Viki':
            if cut_line[2] == '貼圖':
                Viki_sticker_count += 1
            elif cut_line[2] == '圖片':
                Viki_image_count += 1
            else:
                for msg in cut_line[2:]:
                    Viki_word_count += len(msg)
    print('Allen說了', Allen_word_count, '個字，傳了', Allen_sticker_count,'個貼圖')
    print('Viki說了', Viki_word_count, '個字，傳了', Viki_sticker_count,'個貼圖')
    print('Allen傳了', Allen_sticker_count,'個貼圖')
    print('Viki傳了', Viki_sticker_count,'個貼圖')
    print('Allen傳了', Allen_image_count,'張圖片')
    print('Viki傳了', Viki_image_count,'張圖片')


def main():
    lines = read_file('LINE.txt')
    analytics(lines)


main()