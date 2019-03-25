def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    new_lines = lines[1:(len(lines)+1):5]
    return new_lines
    
def write_file(filename, new_lines):
    with open(filename, 'w', encoding='utf-8') as f:
        for line in new_lines:
            f.write(line + '\n')
            
def main():
    lines = read_file('input.txt')
    new_lines = convert(lines)
    write_file('output.txt', new_lines)

main()