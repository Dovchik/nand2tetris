from hack_parser import parse_asm
import argparse
import ntpath

parser = argparse.ArgumentParser(
    description='Assamble CPU instruction for Hack CPU from Hack Machine Language')
parser.add_argument('file', metavar='f', type=str,
                    help='A file to be assembled from')

args = parser.parse_args()
file_loc = args.file


def main():
    with open(file_loc, 'r') as f:
        file_lines, link_lines = prepare_file_lines(f)
    m_lines = parse_asm(file_lines, link_lines)
    with open(change_extension(file_loc), 'w') as w:
        write_lines_to_file(w, m_lines)


def change_extension(file_loc: str):
    inx = file_loc.rfind('.')
    to_replace = file_loc[inx+1:]
    return replace_last(file_loc, to_replace, "hack")


def replace_last(source_string, replace_what, replace_with):
    head, _sep, tail = source_string.rpartition(replace_what)
    return head + replace_with + tail


def write_lines_to_file(dest_file, ml_lines):
    for line in ml_lines:
        print(line + '\n')
        dest_file.write(line)
        dest_file.write('\n')


def prepare_file_lines(file):
    file_lines = []
    link_lines = {}
    prepared = []
    for i, line in enumerate(file):
        trimed = "".join(line.split())
        if trimed.startswith('//'):
            continue
        if len(trimed) == 0:
            continue
        trimed = trimed.split('//')[0]
        prepared.append(trimed)
    c = 0
    for i, line in enumerate(prepared):
        if line.startswith('(') and line.endswith(')'):
            link_lines[line[1:-1]] = i - c
            c += 1
        else:
            file_lines.append(line)
    return file_lines, link_lines


main()