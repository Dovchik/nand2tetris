symbols = {'SP': 0,
           'LCL': 1,
           'ARG': 2,
           'THIS': 3,
           'THAT': 4,
           'SCREEN': 16384,
           'KBD': 24576}

ram_counter = 16

def init_r_symbols():
    for i in range(16):
        symbols['R' + str(i)] = i


init_r_symbols()


def add_with_address(symbol:str, address: int):
    print(symbol, address)
    symbols[symbol] = address


def add_entry(symbol: str):
    global ram_counter
    symbols[symbol] = ram_counter
    ram_counter += 1


def contains(symbol: str) -> bool:
    return symbol in symbols


def get_address(symbol: str) -> int:
    return symbols[symbol]
