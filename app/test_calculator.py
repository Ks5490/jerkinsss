def test_add():
    assert add(4, 2) == 6
    assert add(4, 4) == 8
    assert add(4, 0) == 6
    assert add(3, 3) == 6
    assert add(1, 1) == 2

   
def add(num1, num2):
    return num1 + num2
