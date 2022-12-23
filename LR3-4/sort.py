def sort(array: list | tuple, is_lambda=False):
    if is_lambda:
        return tuple(sorted(array, key=lambda i: -abs(i)))  # Одна строка с анонимной функцией
    return tuple(sorted(array, key=abs, reverse=True))  # Одна строка без анонимной функции


if __name__ == '__main__':
    print("Testing...")

    # Testing
    assert sort((4, -30, 30, 100, -100, 123, 1, 0, -1, -4)) == (123, 100, -100, -30, 30, 4, -4, 1, -1, 0), \
        "\n[TestError][#1] -> -Failed-"
    assert sort((4, -30, 30, 100, -100, 123, 1, 0, -1, -4),
                is_lambda=True) == (123, 100, -100, -30, 30, 4, -4, 1, -1, 0), \
        "\n[TestError][#2] -> -Failed-"

    print("All tests passed!\n")

    print("Run with array (4, -30, 30, 100, -100, 123, 1, 0, -1, -4):")
    print(sort((4, -30, 30, 100, -100, 123, 1, 0, -1, -4)))
