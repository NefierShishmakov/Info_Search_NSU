import pascal_triangle_functions


def main() -> None:
    try:
        n = int(input("Enter positive integer number: "))
    except ValueError:
        print("You need to enter positive integer number!")
        return

    if n <= 0:
        print("You need to enter positive integer number!")
        return

    pascal_triangle_list: list[list[int]] = pascal_triangle_functions.get_pascal_triangle_list(n)
    pascal_triangle_functions.print_pascal_triangle_list(pascal_triangle_list, n)


if __name__ == '__main__':
    main()
