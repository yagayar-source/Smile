

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



from mycode import run_code

def test_output_from_start_pos():
    assert run_code("*_*") == chr(0)

def test_increment():
    assert run_code("^_^  *_*") == chr(1)

def test_decrement():
    assert run_code("!_!  *_*") == chr(255)

def test_increment2():
    assert run_code("^_^ ^_^ ^_^  *_*") == chr(3)

def test_multiple_out():
    assert run_code("*_* *_* *_* *_*") == chr(0) * 4

def test_double_output():
    assert run_code('^_^ *_*  *_*') == chr(1) + chr(1)

def test_move_right():
    assert run_code('^_^ *_* D_D  *_*') == chr(1) + chr(0)

def test_move_left():
    assert run_code('^_^ *_* D_D A_A  *_*') == chr(1) + chr(1)

def test_input():
    assert run_code('?_? ^_^  *_*', 'A') == chr(66)
def test_loops():
    assert run_code('^_^ ^_^ (-: D_D ^_^ ^_^ ^_^ ^_^ A_A :-) D_D *_*') == chr(4)

def test_copy_right():
    assert run_code('^_^ ^_^ >_> D_D *_*') == chr(2)

def test_copy_left():
    assert run_code('^_^ ^_^ <_< A_A *_*') == chr(2)

def test_nested_loops_classic():
    code = '^_^  (-: (-:  :-)  :-)  *_*'
    assert run_code(code) == chr(1)
