lines = []
with open('LINE_2.txt', 'r', encoding = 'utf-8-sig') as file:
    for line in file:
        lines.append(line.strip())

for line in lines:
    cut_line = line.split(" ")
    print(cut_line)
    time = cut_line[0][:5]
    print(time)
    name = cut_line[0][5:]
    print(name)


