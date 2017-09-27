from binary_strings import generate_binary_strings

def test_zero_n():
    assert generate_binary_strings(0) == []

def test_1_n():
    assert generate_binary_strings(1) == ["0", "1"]

def test_non_zero_n():
    assert generate_binary_strings(2) == ["00", "01", "10", "11"]
