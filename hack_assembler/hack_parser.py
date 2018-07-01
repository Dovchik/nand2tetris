from CommandType import CommandType


def parse_asm(file_lines) -> []:
    ml_lines = []
    for line in file_lines:
        command_type = identify_command(line)
        if command_type == CommandType.C_COMMAND:
            ml_lines.append(build_command_bytes(line))
        if command_type == CommandType.A_COMMAND:
            ml_lines.append(symbol(line))
    return ml_lines


def identify_command(line: str) -> CommandType:
    print(line)
    if line.startswith('@'):
        return CommandType.A_COMMAND
    if "=" in line or ";" in line:
        return CommandType.C_COMMAND
    if line.startswith('(') and line.endswith(')'):
        return CommandType.L_COMMAND
    raise Exception("Not a supported commnd")


def symbol(line: str):
    s_line = "0"
    n_line = line[1:]
    s_line += format(int(n_line), '015b')
    return s_line


def dest(line) -> str:
    dest_exp = ""
    if '=' in line:
        dest_exp = line.split("=")[0]
    else:
        return "000"
    dest_str = "1" if "A" in dest_exp else "0"
    dest_str += "1" if "D" in dest_exp else "0"
    dest_str += "1" if "M" in dest_exp else "0"
    return dest_str


one_comp = ["M", "!M", "-M", "M+1", "M-1", "D+M", "D-M", "M-D", "D&M", "D|M"]
zero_comp = ['0', '1', '-1', 'D', 'A', '!D', '!A', '-D', '-A', 'D+1', 'A+1',
                       'D-1', 'A-1', 'D+A', 'D-A', 'A-D', 'D&A', 'D|A']


def comp(line: str) -> str:
    if '=' in line:
        w_line = line.split('=')[1]
    else:
        w_line = line.split(';')[0]
    comp_type = "0" if w_line in zero_comp else "1"
    return comp_type + get_code(w_line)


def get_code(w_line):
    if zero_comp[0] == w_line:
        return "101010"
    if zero_comp[1] == w_line:
        return "111111"
    if zero_comp[2] == w_line:
        return "111010"
    if zero_comp[3] == w_line:
        return "001100"
    if zero_comp[4] == w_line or one_comp[0] == w_line:
        return "110000"
    if zero_comp[5] == w_line:
        return "001101"
    if zero_comp[6] == w_line or one_comp[1] == w_line:
        return "110001"
    if zero_comp[7] == w_line:
        return "001111"
    if zero_comp[8] == w_line or one_comp[2] == w_line:
        return "110011"
    if zero_comp[9] == w_line:
        return "011111"
    if zero_comp[10] == w_line or one_comp[3] == w_line:
        return "110111"
    if zero_comp[11] == w_line:
        return "001110"
    if zero_comp[12] == w_line or one_comp[4] == w_line:
        return "110010"
    if zero_comp[13] == w_line or one_comp[5] == w_line:
        return "000010"
    if zero_comp[14] == w_line or one_comp[6] == w_line:
        return "010011"
    if zero_comp[15] == w_line or one_comp[7] == w_line:
        return "000111"
    if zero_comp[16] == w_line or one_comp[8] == w_line:
        return "000000"
    if zero_comp[17] == w_line or one_comp[9] == w_line:
        return "010101"
    raise Exception("Incorect syntax")


def jump(line: str) -> str:
    if not ';' in line:
        return "000"
    line = line.split(';')[1]
    if "JGT" in line:
        return "001"
    if "JEQ" in line:
        return "010"
    if "JGE" in line:
        return "011"
    if "JLT" in line:
        return "100"
    if "JNE" in line:
        return "101"
    if "JLE" in line:
        return "110"
    if "JMP" in line:
        return "111"
    return "000"


def build_command_bytes(line: str) -> str:
    initial_str = ""
    # append 1 because it's command type
    initial_str += "111"
    initial_str += comp(line)
    initial_str += dest(line)
    initial_str += jump(line)
    return initial_str
