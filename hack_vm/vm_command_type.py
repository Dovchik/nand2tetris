from enum import Enum

class vm_command_type(Enum):
    Arithmetic = 0,
    Push = 1,
    Pop = 2,
    Label = 3,
    Goto = 4,
    If = 5,
    Function = 6,
    Return = 7,
    Call = 8
