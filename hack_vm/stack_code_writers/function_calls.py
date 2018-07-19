from vm_command_type import vm_command_type
import vm_primitive_ml as primitive_ml


def write_function_calls_commands(line_def):
    c_type = line_def['command_type']
    args = line_def['arg']
    if c_type == vm_command_type.Function:
        write_function(args[0], args[1])
    if c_type == vm_command_type.Call:
        write_call(args[0], args[1])
    if c_type == vm_command_type.Return:
        write_return()


def write_function(name, var_count):
    primitive_ml.add_symbol_link(name)
    while var_count > 0:
        primitive_ml.write_to_stack('0')
        var_count -= 1
    return


def write_call(name, var_count):
    return


def write_return():
    #frame = lcl
    primitive_ml.add_line('@LCL')
    primitive_ml.write_c_command('D', 'M')
    primitive_ml.add_line('@FRAME')
    primitive_ml.write_c_command('M', 'D')
    #ret = frame - 5
    primitive_ml.add_line('@RET')
    primitive_ml.write_c_command('M', 'D')
    primitive_ml.write_const_to(5, 'D')
    primitive_ml.add_line('@RET')
    primitive_ml.write_c_command('M', 'M+D')
    #Arg = pop
    primitive_ml.read_stack_to('D')
    primitive_ml.add_line('@ARG')
    primitive_ml.write_c_command('M', 'D')
    #sp = arg + 1
    return
