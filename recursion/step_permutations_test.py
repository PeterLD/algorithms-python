from step_permutations import step_permutations

def test_step_permutations():
    assert step_permutations(0) == 0
    assert step_permutations(1) == 1
    assert step_permutations(2) == 2
    assert step_permutations(3) == 4
