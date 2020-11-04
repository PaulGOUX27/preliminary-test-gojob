def closest_to_zero(values):
    if not values or values is None:
        return 0

    closest_value = values[0]

    for value in values[1:]:
        if value == 0:
            return 0

        if abs(value) < abs(closest_value):
            closest_value = value

        if abs(value) == abs(closest_value) and value > 0:
            closest_value = value

    return closest_value


def run_tests(func):
    assert func([]) == 0
    assert func(None) == 0
    assert func([1]) == 1
    assert func([-6]) == -6
    assert func([3, -4, 0]) == 0
    assert func([8, 5, 10]) == 5
    assert func([5, 4, -9, 6, -10, -1, 8]) == -1
    assert func([8, 2, 3, -2]) == 2
    assert func([2, 0]) == 0
    assert func([8, -2, 3, 2]) == 2
    assert func([1, 4, 5, 8]) == 1
    assert func([8, 5, 4, 1]) == 1


if __name__ == '__main__':
    run_tests(closest_to_zero)

    print('All tests succeed')
