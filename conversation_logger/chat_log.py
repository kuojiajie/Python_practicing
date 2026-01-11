def read_file(file_name):
    lines = []
    with open(file_name, 'r', encoding = 'utf-8-sig') as file:
        for line in file:
            lines.append(line.strip())
    return lines


def convert(lines):
    new_line = []
    name = None
    for line in lines:
        if line == 'Allen':
            name = 'Allen'
            continue
        elif line == 'Tom':
            name = 'Tom'
            continue
        if name:
            new_line.append(name + ':' + line)
    return new_line


def write_file(filename, new_line):
    with open(filename, 'w') as file:
        for line in new_line:
            file.write(line + '\n')


def main():
    lines = read_file('input.txt')
    new_line = convert(lines)
    write_file('output.txt', new_line)



main()