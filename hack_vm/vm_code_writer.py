import vm_primitive_ml as primitive_ml
from ml_lines import add_line
from vm_command_type import vm_command_type

commands = ['empty']
file_name = 'No_FILE_NAME'


def set_file_name(f_name):
    global file_name
    file_name = f_name.split('.')[0]


def write_push_command(line_def):
    if line_def['command_type'] != vm_command_type.Push:
        return
    segment = line_def['arg'][0]
    location = line_def['arg'][1]
    if segment == 'constant':
        add_line('@' + location)
        add_line('D=A')
        primitive_ml.write_to_stack('D')
    elif segment == 'temp':
        write_push_temp(location)
    elif segment == 'pointer':
        write_push_pointer(location)
    elif segment == 'static':
        write_push_static(location)
    else:
        write_push_virtual(segment, location)


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
    primitive_ml.read_stack_to('D')
    primitive_ml.read_stack_and_write('D', 'M-D')
    primitive_ml.write_bool_jumps('JLT')


def write_greater_then_command(line_def):
    if line_def['arg'][0] != 'gt':
        return
    primitive_ml.read_stack_to('D')
    # a > b => a - b > 0 => m=a d=b
    primitive_ml.read_stack_and_write('D', 'M-D')
    primitive_ml.write_bool_jumps('JGT')


def write_eq_command(line_def):
    if line_def['arg'][0] != 'eq':
        return
    primitive_ml.read_stack_to('D')
    primitive_ml.read_stack_and_write('D', 'D-M')
    primitive_ml.write_bool_jumps('JEQ')


def write_add_command(line_def):
    if line_def['arg'][0] == 'add':
        primitive_ml.read_stack_to('D')
        primitive_ml.read_stack_and_write('M', 'M+D')


def write_sub_command(line_def):
    if line_def['arg'][0] != 'sub':
        return
    primitive_ml.read_stack_to('D')
    primitive_ml.read_stack_and_write('M', 'M-D')


def write_and_command(line_def):
    if line_def['arg'][0] != 'and':
        return
    primitive_ml.read_stack_to('D')
    primitive_ml.read_stack_and_write('M', 'M&D')


def write_neg_command(line_def):
    if line_def['arg'][0] != 'neg':
        return
    primitive_ml.read_stack_and_write('M', '-M')


def write_or_command(line_def):
    if line_def['arg'][0] != 'or':
        return
    primitive_ml.read_stack_to('D')
    primitive_ml.read_stack_and_write('M', 'D|M')


def write_not_command(line_def):
    if line_def['arg'][0] != 'not':
        return
    primitive_ml.read_stack_and_write('M', '!M')


def write_push_temp(location):
    primitive_ml.point_to_temp(int(location))
    primitive_ml.write_c_command('D', 'M')
    primitive_ml.write_to_stack('D')


def write_push_pointer(location):
    primitive_ml.point_to_pointer(int(location))
    primitive_ml.write_c_command('D', 'M')
    primitive_ml.write_to_stack('D')


def write_pop_temp(location):
    primitive_ml.read_stack_to('D')
    primitive_ml.point_to_temp(int(location))
    primitive_ml.write_c_command('M', 'D')


def write_push_virtual(segment, location):
    primitive_ml.write_const_to(location, 'D')
    primitive_ml.point_to_segment(segment)
    primitive_ml.write_c_command('D', 'M+D')
    primitive_ml.point_to_segment(segment, True)
    primitive_ml.write_c_command('A', 'D')
    primitive_ml.write_c_command('D', 'M')
    primitive_ml.write_to_stack('D')


def write_pop_command(line_def):
    if line_def['command_type'] != vm_command_type.Pop:
        return
    segment = line_def['arg'][0]
    location = line_def['arg'][1]
    if segment == 'temp':
        write_pop_temp(location)
    elif segment == 'pointer':
        write_pop_pointer(location)
    elif segment == 'static':
        write_pop_static(location)
    else:
        write_pop_virtual(segment, location)


def write_push_static(location):
    global file_name
    primitive_ml.point_static(file_name, location)
    primitive_ml.write_c_command('D', 'M')
    primitive_ml.write_to_stack('D')


def write_pop_pointer(location):
    primitive_ml.read_stack_to('D')
    primitive_ml.point_to_pointer(int(location))
    primitive_ml.write_c_command('M', 'D')


def write_pop_virtual(segment, location):
    add_line('@' + location)
    add_line('D=A')
    primitive_ml.point_to_segment(segment)
    primitive_ml.write_c_command('D', 'M+D')
    primitive_ml.point_to_segment(segment, True)
    primitive_ml.write_c_command('M', 'D')
    primitive_ml.read_stack_to('D')
    primitive_ml.point_to_segment(segment, True)
    primitive_ml.write_c_command('A', 'M')
    primitive_ml.write_c_command('M', 'D')


def write_pop_static(location):
    primitive_ml.read_stack_to('D')
    global file_name
    primitive_ml.point_static(file_name, location)
    primitive_ml.write_c_command('M', 'D')
