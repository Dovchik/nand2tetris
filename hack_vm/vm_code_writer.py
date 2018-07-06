from vm_command_type import vm_command_type

ml_lines = []
commands = ['empty']
equality_counter = 0
next_counter = 0


def increase_stack_pointer():
    ml_lines.append("@SP")
    ml_lines.append("M=M+1")


def descrease_stack_pointer():
    ml_lines.append("@SP")
    ml_lines.append("M=M-1")

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
        ml_lines.append('D=D-A')
        global equality_counter
        eq_label_true = 'EQ.TRUE.'+str(equality_counter)
        eq_label_false = 'EQ.FALSE.'+str(equality_counter)
        ml_lines.append('@' + eq_label_true)
        ml_lines.append('D;JEQ')
        ml_lines.append('@' + eq_label_false)
        ml_lines.append('0;JMP')
        add_symbol_link(eq_label_true)
        set_sp_bool(True)
        add_next_symbol()
        add_symbol_link(eq_label_false)
        set_sp_bool(False)
        symb_next = add_next_symbol()
        add_symbol_link(symb_next)
        global next_counter
        next_counter += 1
        equality_counter += 1


def add_next_symbol():
    global next_counter
    symb_next = 'NEXT.' + str(next_counter)
    ml_lines.append('@' + symb_next)
    ml_lines.append('0;JMP')
    return symb_next


def add_symbol_link(label):
    ml_lines.append(get_symbol_link(label))


def set_sp_bool(pos):
    ml_lines.append('@SP')
    if pos:
        ml_lines.append('M=0')
    else:
        ml_lines.append('M=-1')


def get_symbol_link(symbol):
    return '(' + symbol + ')'


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
            
