from nested_sum import nested_sum

def test_non_nested():
    assert nested_sum([1, 2, 3]) == 6

def test_nested():
    assert nested_sum([1, [2, 3], [4, [5, [6]]]]) == 21
