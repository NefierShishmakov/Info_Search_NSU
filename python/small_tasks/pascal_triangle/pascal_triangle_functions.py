def get_pascal_triangle_list(n: int) -> list[list[int]]:
    pascal_triangle_list: list[list[int]] = [[0, 1, 0]]

    for i in range(n - 1):
        prev_list: list[int] = pascal_triangle_list[i]
        pascal_triangle_list.append(__get_new_pascal_triangle_line_as_integer_list(prev_list))
        __remove_zeros_from_list(prev_list)

    __remove_zeros_from_list(pascal_triangle_list[n - 1])
    return pascal_triangle_list


def __get_new_pascal_triangle_line_as_integer_list(prev_line_as_integer_list: list[int]) -> list[int]:
    prev_list_length: int = len(prev_line_as_integer_list)

    new_list: list[int] = [0]
    for j in range(prev_list_length - 1):
        new_list.append(prev_line_as_integer_list[j] + prev_line_as_integer_list[j + 1])
    new_list.append(0)
    return new_list


def __remove_zeros_from_list(list: list[int]) -> None:
    list.remove(0)
    list.remove(0)


def print_pascal_triangle_list(pascal_triangle_list: list[list[int]], lines_num: int) -> None:
    for i in range(lines_num):
        print(' ' * (lines_num - 1 - i) + ' '.join(str(e) for e in pascal_triangle_list[i]))
