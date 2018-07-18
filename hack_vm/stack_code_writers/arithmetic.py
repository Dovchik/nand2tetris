import vm_primitive_ml as primitive_ml
from vm_command_type import vm_command_type


def write_arithmetic_commands(line_def):
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


def write_eq_command(line_def):
    if line_def['arg'][0] != 'eq':
        return
    primitive_ml.read_stack_to('D')
    primitive_ml.read_stack_and_write('D', 'D-M')
    primitive_ml.write_bool_jumps('JEQ')


def write_greater_then_command(line_def):
    if line_def['arg'][0] != 'gt':
        return
    primitive_ml.read_stack_to('D')
    # a > b => a - b > 0 => m=a d=b
    primitive_ml.read_stack_and_write('D', 'M-D')
    primitive_ml.write_bool_jumps('JGT')


def write_not_command(line_def):
    if line_def['arg'][0] != 'not':
        return
    primitive_ml.read_stack_and_write('M', '!M')


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
