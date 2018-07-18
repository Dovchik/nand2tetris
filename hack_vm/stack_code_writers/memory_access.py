from vm_command_type import vm_command_type
from ml_lines import add_line
import vm_primitive_ml as primitive_ml

file_name = 'NO_FILE_NAME'

def set_file_name(name):
    global file_name
    file_name = name


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