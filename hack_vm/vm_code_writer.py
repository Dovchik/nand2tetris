from vm_command_type import vm_command_type

ml_lines = []
commands = ['empty']


def prev_constant():
    return commands[-1] == 'constant'


def get_ml_lines():
    return ml_lines


def write_command(line_def):
    print(line_def)
    write_push_command(line_def)
    write_arithmetic_command(line_def)
    commands.append(line_def['arg'][0])


def write_arithmetic_command(line_def):
    if line_def['command_type'] == vm_command_type.Arithmetic:
        write_add_command(line_def)
        write_eq_command(line_def)


def write_eq_command(line_def):
    if line_def['arg'][0] == 'eq':
        ml_lines.append('D=D&A')


def write_add_command(line_def):
    if line_def['arg'][0] == 'add':
        ml_lines.append('D=D+A')


def write_push_command(line_def):
    if line_def['command_type'] == vm_command_type.Push:
        arg = line_def['arg'][0]
        if arg == 'constant':
            ml_lines.append('@' + line_def['arg'][1])
            if not prev_constant():
                ml_lines.append('D=A')
