from vm_command_type import vm_command_type

arithmetic = ['add', 'sub', 'neg', 'eq', 'gt', 'lt', 'and', 'or', 'not']


def get_arg(command_type, line: [str]):
    if command_type == vm_command_type.Arithmetic:
        return line
    else:
        return line[1:]


def parse_line(line):
    print(line)
    l = prepare_line(line)
    print(l)
    if not l:
        return None
    line_def = {}
    line_def['command_type'] = command_type(l[0])
    line_def['arg'] = get_arg(line_def['command_type'], l)
    return line_def


def prepare_line(line) -> [str]:
    line = line.split('//')[0]
    if '\n' in line:
        line = line[:-1]
    return list(filter(None, line.split(' ')))


def command_type(command: str):
    if command in arithmetic:
        return vm_command_type.Arithmetic
    if command == 'push':
        return vm_command_type.Push
    if command == 'pop':
        return vm_command_type.Pop
    if command == 'label':
        return vm_command_type.Label
    if command == 'if-goto':
        return vm_command_type.If
    if command == 'goto':
        return vm_command_type.Goto
    if command == 'function':
        return vm_command_type.Function
    if command == 'return':
        return vm_command_type.Return
    if command == 'call':
        return vm_command_type.Call
