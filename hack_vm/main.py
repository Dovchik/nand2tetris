import argparse
from os.path import isfile, isdir, join
from os import listdir
from vm_parser import parse_line
from io import open
from vm_parser import parse_line
from ml_lines import get_lines, add_line
from vm_code_writer import write_command

parser = argparse.ArgumentParser(
    description='Translate VM code into Hack Machine Language')
parser.add_argument('source', metavar='s', type=str,
                    help='A file or folder that will be translated')


def change_extension(file_loc: str):
    inx = file_loc.rfind('.')
    to_replace = file_loc[inx+1:]
    return replace_last(file_loc, to_replace, "asm")


def replace_last(source_string, replace_what, replace_with):
    head, _sep, tail = source_string.rpartition(replace_what)
    return head + replace_with + tail


def is_vm_file(source):
    return source.endswith('.vm')


def get_files(source):
    vm_files = [file for file in listdir(source)
                if isfile(join(source, file)) and is_vm_file(file)]
    for vm_file in vm_files:
        print(vm_file)


args = parser.parse_args()
source = args.source


def write_and_command(file):
    file.write('(END)\n@END\n0;JMP')


if isfile(source) and is_vm_file(source):
    print("Is file " + source)
    with open(source, 'r') as source_file:
        for line in source_file:
            parsed = parse_line(line)
            if parsed is None:
                continue
            write_command(parsed)
    ml_lines = get_lines()
    print(ml_lines)
    with open(change_extension(source), 'w') as dest_file:
        for ml in ml_lines:
            dest_file.write(ml)
            dest_file.write('\n')
        write_and_command(dest_file)


if isdir(source):
    get_files(source)
