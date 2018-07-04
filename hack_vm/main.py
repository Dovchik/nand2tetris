import argparse
from os.path import isfile, isdir, join
from os import listdir

parser = argparse.ArgumentParser(
    description='Translate VM code into Hack Machine Language')
parser.add_argument('source', metavar='s', type=str,
                    help='A file or folder that will be translated')

def is_vm_file(source):
    return source.endswith('.vm')


def get_files(source):
    vm_files = [file for file in listdir(source) 
                if isfile(join(source, file)) and is_vm_file(file)]
    for vm_file in vm_files:
        print(vm_file)

args = parser.parse_args()
source = args.source

if isfile(source) and is_vm_file(source):
    print("Is file " + source)
if isdir(source):
    get_files(source)


