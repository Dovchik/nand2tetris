from hack_parser import parse_asm

def main():
    with open('MaxL.asm', 'r') as f:
        file_lines = []
        for line in f:
            trimed = "".join(line.split())
            if trimed.startswith('//'):
                continue
            if len(trimed) == 0:
                continue
            file_lines.append(trimed)
        m_lines = parse_asm(file_lines)
        with open('MaxL.hack', 'w') as w:
            for line in m_lines:
                print(line + '\n')
                w.write(line)
                w.write('\n')

main()

