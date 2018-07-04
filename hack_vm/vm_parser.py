
def prepare_line(line) -> [str]:
    line = line.split('//')[0]
    return [x.strip() for  x in line.split(' ')]