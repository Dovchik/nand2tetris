from vm_command_type import vm_command_type
import vm_primitive_ml as primitive_ml


def write_program_flow_command(line_def):
    c_type = line_def['command_type']
    args = line_def['arg']
    if c_type == vm_command_type.Goto:
        write_goto(args[0])
    if c_type == vm_command_type.If:
        write_if(args[0])
    if c_type == vm_command_type.Label:
        write_label(args[0])


def write_goto(location):
    primitive_ml.unconditional_jump(location)


def write_if(location):
    primitive_ml.read_stack_to('D')
    primitive_ml.add_line('@' + location)
    primitive_ml.add_line('D;JNE')


def write_label(label):
    primitive_ml.add_symbol_link(label)
