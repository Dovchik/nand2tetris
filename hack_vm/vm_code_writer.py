from vm_command_type import vm_command_type
from ml_lines import add_line
from vm_primitive_ml import increase_stack_pointer, descrease_stack_pointer, read_stack_to, point_stack_current, write_to_stack, get_symbol_link, read_stack_and_write, write_bool_jumps, write_c_command, point_to_segment, point_to_local_tmp, pop_stack_value, write_const_to, point_to_temp


commands = ['empty']


def prev_constant():
    return commands[-1] == 'constant'


def write_command(line_def):
    print(line_def)
    write_push_command(line_def)
    write_pop_command(line_def)
    write_arithmetic_command(line_def)
    commands.append(line_def['arg'][0])


def write_arithmetic_command(line_def):
    if line_def['command_type'] == vm_command_type.Arithmetic:
        write_add_command(line_def)
        write_eq_command(line_def)
        write_less_then_command(line_def)
        write_greater_then_command(line_def)
        write_sub_command(line_def)
        write_and_command(line_def)
        write_neg_command(line_def)
        write_or_command(line_def)
        write_not_command(line_def)


def write_less_then_command(line_def):
    if line_def['arg'][0] != 'lt':
        return
    read_stack_to('D')
    read_stack_and_write('D', 'M-D')
    write_bool_jumps('JLT')


def write_greater_then_command(line_def):
    if line_def['arg'][0] != 'gt':
        return
    read_stack_to('D')
    # a > b => a - b > 0 => m=a d=b
    read_stack_and_write('D', 'M-D')
    write_bool_jumps('JGT')


def write_eq_command(line_def):
    if line_def['arg'][0] != 'eq':
        return
    read_stack_to('D')
    read_stack_and_write('D', 'D-M')
    write_bool_jumps('JEQ')


def write_add_command(line_def):
    if line_def['arg'][0] == 'add':
        read_stack_to('D')
        read_stack_and_write('M', 'M+D')


def write_sub_command(line_def):
    if line_def['arg'][0] != 'sub':
        return
    read_stack_to('D')
    read_stack_and_write('M', 'M-D')


def write_and_command(line_def):
    if line_def['arg'][0] != 'and':
        return
    read_stack_to('D')
    read_stack_and_write('M', 'M&D')


def write_neg_command(line_def):
    if line_def['arg'][0] != 'neg':
        return
    read_stack_and_write('M', '-M')


def write_or_command(line_def):
    if line_def['arg'][0] != 'or':
        return
    read_stack_to('D')
    read_stack_and_write('M', 'D|M')


def write_not_command(line_def):
    if line_def['arg'][0] != 'not':
        return
    read_stack_and_write('M', '!M')


def write_push_command(line_def):
    if line_def['command_type'] != vm_command_type.Push:
        return
    segment = line_def['arg'][0]
    location = line_def['arg'][1]
    if segment == 'constant':
        add_line('@' + location)
        add_line('D=A')
        write_to_stack('D')
    elif segment == 'temp':
        write_push_temp(location)
    else:
        write_push_virtual(segment, location)


def write_push_temp(location):
    point_to_temp(int(location))
    write_c_command('D', 'M')
    write_to_stack('D')


def write_pop_temp(location):
    read_stack_to('D')
    point_to_temp(int(location))
    write_c_command('M', 'D')


def write_push_virtual(segment, location):
    write_const_to(location, 'D')
    point_to_segment(segment)
    write_c_command('D', 'M+D')
    point_to_segment(segment, True)
    write_c_command('A', 'D')
    write_c_command('D', 'M')
    write_to_stack('D')


def write_pop_command(line_def):
    if line_def['command_type'] != vm_command_type.Pop:
        return
    segment = line_def['arg'][0]
    location = line_def['arg'][1]
    if segment == 'temp':
        write_pop_temp(location)
    else:
        write_pop_virtual(segment, location)


def write_pop_virtual(segment, location):
    add_line('@' + location)
    add_line('D=A')
    point_to_segment(segment)
    write_c_command('D', 'M+D')
    point_to_segment(segment, True)
    write_c_command('M', 'D')
    read_stack_to('D')
    point_to_segment(segment, True)
    write_c_command('A', 'M')
    write_c_command('M', 'D')
