from ml_lines import add_line

stack_pointer = 256
equality_counter = 0
next_counter = 0
temp_base = 5
pointer_base = 3


def init_stack_pointer():
    add_line('@' + str(stack_pointer))
    add_line('D=A')
    add_line('@SP')
    add_line('M=D')


init_stack_pointer()


def increase_stack_pointer():
    global stack_pointer
    stack_pointer += 1
    add_line("@SP")
    add_line("M=M+1")


def descrease_stack_pointer():
    global stack_pointer
    stack_pointer -= 1
    add_line("@SP")
    add_line("M=M-1")


def pop_stack_value(dest: str):
    point_top_stack_val()
    write_c_command(dest, 'M')


def point_top_stack_val():
    add_line('@' + str(stack_pointer - 1))


def read_stack_to(dest: str, discrease_pointer=True):
    if discrease_pointer:
        descrease_stack_pointer()
    point_stack_current()
    add_line(dest + '=M')


def write_to_stack(source):
    point_stack_current()
    add_line("M=" + source)
    increase_stack_pointer()


def add_next_symbol():
    global next_counter
    symb_next = 'NEXT.' + str(next_counter)
    add_line('@' + symb_next)
    add_line('0;JMP')
    return symb_next


def read_stack_and_write(dest, op):
    descrease_stack_pointer()
    point_stack_current()
    add_line(dest + '=' + op)
    if dest == "M":
        increase_stack_pointer()


def point_stack_current():
    global stack_pointer
    add_line('@' + str(stack_pointer))


def get_symbol_link(symbol):
    return '(' + symbol + ')'


def add_symbol_link(label):
    add_line(get_symbol_link(label))


def write_bool_jumps(jump_cond):
    eq_label_true = true_label()
    eq_label_false = false_label()
    add_line('@' + eq_label_true)
    add_line('D;' + jump_cond)
    add_line('@' + eq_label_false)
    add_line('0;JMP')
    add_symbol_link(eq_label_true)
    set_bool_to_stack(True)
    add_next_symbol()
    add_symbol_link(eq_label_false)
    set_bool_to_stack(False)
    symb_next = add_next_symbol()
    add_symbol_link(symb_next)
    increase_stack_pointer()
    global next_counter
    next_counter += 1
    global equality_counter
    equality_counter += 1


def set_bool_to_stack(pos):
    vm_true_value = '-1'
    vm_false_value = '0'
    if pos:
        source = vm_true_value
    else:
        source = vm_false_value
    point_stack_current()
    add_line("M=" + source)


def write_const_to(const, dest):
    add_line('@' + const)
    write_c_command(dest, 'A')


def point_to_temp(location):
    global temp_base
    point_to_base(temp_base, location)


def point_to_pointer(location):
    global pointer_base
    point_to_base(pointer_base, location)


def point_static(name, location):
    add_line('@' + name + '.' + location)


def point_to_base(base, location):
    add_line('@' + str(base + location))


def false_label():
    return 'BOOL.FALSE.'+str(equality_counter)


def point_to_segment(segment: str, tmp=False):
    s = ''
    if segment == 'local':
        s = 'LCL'
    if segment == 'this':
        s = 'THIS'
    if segment == 'that':
        s = 'THAT'
    if segment == 'argument':
        s = 'ARG'
    if segment == 'temp':
        s = 'TEMP'
    if tmp:
        s = s + '_TMP'
    add_line('@' + s)


def point_to_local_tmp():
    add_line('@lcl_temp')


def write_c_command(dest, source):
    add_line(dest + '=' + source)


def true_label():
    return 'BOOL.TRUE.'+str(equality_counter)
