import vm_primitive_ml as primitive_ml
from ml_lines import add_line
from vm_command_type import vm_command_type
import stack_code_writers.arithmetic as arithmetic
import stack_code_writers.memory_access as memory_access
import stack_code_writers.program_flow as program_flow
import stack_code_writers.function_calls as function_calls

file_name = 'No_FILE_NAME'


def set_file_name(f_name):
    global file_name
    file_name = f_name.split('.')[0]
    memory_access.set_file_name(file_name)

def sys_init():
    primitive_ml.init_stack_pointer()
    function_calls.write_call('Sys.init', 0)

sys_init()

def write_command(line_def):
    print(line_def)
    memory_access.write_push_command(line_def)
    memory_access.write_pop_command(line_def)
    arithmetic.write_arithmetic_commands(line_def)
    program_flow.write_program_flow_command(line_def)
    function_calls.write_function_calls_commands(line_def)
