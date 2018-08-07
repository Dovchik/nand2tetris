from vm_command_type import vm_command_type
import vm_primitive_ml as primitive_ml

return_counter = 0

def write_function_calls_commands(line_def):
    c_type = line_def['command_type']
    args = line_def['arg']
    if c_type == vm_command_type.Function:
        write_function(args[0], int(args[1]))
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
     # push return-address (using label below)
    global return_counter
    return_label = 'return.' + str(return_counter)
    primitive_ml.add_line('@' + return_label)
    primitive_ml.write_c_command('D', 'A')
    primitive_ml.write_to_stack('D')
    # push lcl
    read_symbol_to_stack('LCL')
    read_symbol_to_stack('ARG')
    read_symbol_to_stack('THIS')
    read_symbol_to_stack('THAT')
    # reposition arg
    primitive_ml.add_line('@SP')
    primitive_ml.write_c_command('D', 'M')
    primitive_ml.add_line('@ARG')
    primitive_ml.write_c_command('M', 'D')
    primitive_ml.add_line('@5')
    primitive_ml.write_c_command('D', 'A')
    primitive_ml.add_line('@ARG')
    primitive_ml.write_c_command('M','M-D')
    primitive_ml.add_line('@' + str(var_count))
    primitive_ml.write_c_command('D', 'A')
    primitive_ml.add_line('@ARG')
    primitive_ml.write_c_command('M', 'M-D')

    # reposition lcl

    primitive_ml.add_line('@SP')
    primitive_ml.write_c_command('D', 'M')
    primitive_ml.add_line('@LCL')
    primitive_ml.write_c_command('M', 'D')
    # goto function
    primitive_ml.unconditional_jump(name)
    # declare return label
    primitive_ml.add_symbol_link(return_label)
    return_counter += 1
    return


def read_symbol_to_stack(symbol):
    primitive_ml.add_line('@' + symbol)
    primitive_ml.write_c_command('D', 'M')
    primitive_ml.write_to_stack('D')


def write_return():
    #frame = lcl
    frame()
    # ret = *(frame - 5)\
    save_return_address()
    # Arg = pop / arg pointer  = pop
    reposition_return_val()
    #sp = arg + 1
    restore_sp_of_caller()

    restore_vm_symbols('THAT')

    restore_vm_symbols('THIS')

    restore_vm_symbols('ARG')

    restore_vm_symbols('LCL')

    go_to_return_address()
    return


def go_to_return_address():
    primitive_ml.add_line('@RET')
    primitive_ml.add_line('A=M')
    primitive_ml.add_line('0;JMP')


def restore_vm_symbols(symbol):
    frame_minus()
    primitive_ml.add_line('@' + symbol)
    primitive_ml.add_line('M=D')


def restore_sp_of_caller():
    primitive_ml.add_line('@ARG')
    primitive_ml.add_line('D=M')
    primitive_ml.set_stack_pointer('D+1')


def reposition_return_val():
    primitive_ml.read_stack_to('D')
    primitive_ml.add_line('@ARG')
    primitive_ml.add_line('A=M')
    primitive_ml.add_line('M=D')


def frame():
    primitive_ml.add_line('@LCL')
    primitive_ml.write_c_command('D', 'M')
    primitive_ml.add_line('@FRAME')
    d_to_m()
    primitive_ml.add_line('D=M')


def save_return_address():
    primitive_ml.add_line('@5')
    primitive_ml.add_line('D=D-A')
    primitive_ml.add_line('A=D')
    primitive_ml.add_line('D=M')
    primitive_ml.add_line('@RET')
    primitive_ml.add_line('M=D')


def frame_minus():
    primitive_ml.add_line('@FRAME')
    primitive_ml.add_line('M=M-1')
    primitive_ml.add_line('A=M')
    primitive_ml.add_line('D=M')


def frame_descrese_to_d():
    primitive_ml.add_line('@FRAME')
    primitive_ml.add_line('M=M-1')
    primitive_ml.add_line('A=M')
    primitive_ml.write_c_command('D', 'M')


def d_to_m():
    primitive_ml.write_c_command('M', 'D')


def decrement_d():
    primitive_ml.write_c_command('D', 'D-1')
