def closest_to_zero(values):
    if not values or values is None:
        return 0

    closest_value = values[0]
    closest_value_positive = closest_value

    if closest_value_positive < 0:
        closest_value_positive *= -1

    for value in values[1:]:
        if value == 0:
            return 0
        tmp = value
        if tmp < 0:
            tmp *= -1
        if tmp < closest_value_positive:
            closest_value = value
            closest_value_positive = tmp

        if tmp == closest_value_positive and value > 0:
            closest_value = value

    return closest_value


def closest_to_zero_stackoverflow(values):
    # https://stackoverflow.com/questions/11923657/python-find-integer-closest-to-0-in-list
    if not values or values is None:
        return 0
    return min(values, key=abs)


if __name__ == '__main__':
    assert closest_to_zero([]) == 0
    assert closest_to_zero(None) == 0
    assert closest_to_zero([1]) == 1
    assert closest_to_zero([-6]) == -6
    assert closest_to_zero([3, -4, 0]) == 0
    assert closest_to_zero([8, 5, 10]) == 5
    assert closest_to_zero([5, 4, -9, 6, -10, -1, 8]) == -1
    assert closest_to_zero([8, 2, 3, -2]) == 2
    assert closest_to_zero([2, 0]) == 0

    assert closest_to_zero_stackoverflow([]) == 0
    assert closest_to_zero_stackoverflow(None) == 0
    assert closest_to_zero_stackoverflow([1]) == 1
    assert closest_to_zero_stackoverflow([-6]) == -6
    assert closest_to_zero_stackoverflow([3, -4, 0]) == 0
    assert closest_to_zero_stackoverflow([8, 5, 10]) == 5
    assert closest_to_zero_stackoverflow([5, 4, -9, 6, -10, -1, 8]) == -1
    assert closest_to_zero_stackoverflow([8, 2, 3, -2]) == 2
    assert closest_to_zero_stackoverflow([2, 0]) == 0

    print('All tests succeed')
