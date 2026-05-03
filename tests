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
