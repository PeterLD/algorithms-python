"""
Cracking the Coding Interview, page 109.

A child is running up a staircase with n steps, and can hop either 1 step,
2 steps, or 3 steps at a time. Implement a method to count how many possible
ways the child can run up the stairs.
"""
def step_permutations(num_steps):
    step_possibilities = 0
    step_options = [1, 2, 3]

    for step_option in step_options:
        if step_option == num_steps:
            step_possibilities += 1
        elif step_option < num_steps:
            step_possibilities += step_permutations(num_steps - step_option)

    return step_possibilities
