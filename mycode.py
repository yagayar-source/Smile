def run_code(code, inputt=''):
    code = code.split()
    p = code.count('?_?')
    while p > len(inputt):
        inputt = inputt + '  '

    bufer = inputt
    count_bufer = 0
    i = 0

    rows = 1000
    cols = 1000
    ceils = [[0] * cols for _ in range(rows)]
    row = 0
    col = 0
    s = ''

    while i < len(code):
        if code[i] == "^_^":
            ceils[row][col] = (ceils[row][col] + 1) % 256
        elif code[i] == "!_!":
            ceils[row][col] = (ceils[row][col] - 1) % 256
        elif code[i] == "*_*":
            s += chr(ceils[row][col] % 256)
        elif code[i] == "D_D":
            col = (col + 1) % 1000
        elif code[i] == "A_A":
            col = (col - 1) % 1000
        elif code[i] == "W_W":
            row = (row - 1) % 1000
        elif code[i] == "S_S":
            row = (row + 1) % 1000
        elif code[i] == '?_?':
            if count_bufer < len(bufer):
                ceils[row][col] = ord(bufer[count_bufer])
                count_bufer += 1
        elif code[i] == ">_>":
            ceils[row][(col + 1) % 1000] = ceils[row][col]
        elif code[i] == "<_<":
            ceils[row][(col - 1) % 1000] = ceils[row][col]
        elif code[i] == '(-:':
            if ceils[row][col] == 0:
                depth = 1
                while depth > 0:
                    i += 1
                    if code[i] == '(-:':
                        depth += 1
                    elif code[i] == ':-)':
                        depth -= 1
        elif code[i] == ':-)':
            if ceils[row][col] != 0:
                depth = 1
                while depth > 0:
                    i -= 1
                    if code[i] == ':-)':
                        depth += 1
                    elif code[i] == '(-:':
                        depth -= 1

        i += 1

    return s