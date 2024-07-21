from example import add, sub, mul, div, mod

def test_add():
    assert add(1, 2) == 3
    assert add(0, 0) == 0
    assert add(-1, -1) == -2
    assert add(1, -1) == 0

def test_sub():
    assert sub(1, 2) == -1
    assert sub(0, 0) == 0
    assert sub(-1, -1) == 0
    assert sub(1, -1) == 2

def test_mul():
    assert mul(1, 2) == 2
    assert mul(0, 0) == 0
    assert mul(-1, -1) == 1
    assert mul(1, -1) == -1

def test_div():
    assert div(1, 2) == 0.5
    assert div(0, 1) == 0
    assert div(-1, -1) == 1
    assert div(1, -1) == -1

    # Test division by zero (should raise ValueError)
    try:
        div(1, 0)
        assert False, "Expected ValueError when dividing by zero"
    except ValueError:
        pass

def test_mod():
    assert mod(1, 2) == 1
    assert mod(0, 1) == 0
    assert mod(-1, -1) == 0
