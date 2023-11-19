def bracket_sequence_correct(bracket_sequence: str) -> bool:
    result: bool = False
    while True:
        new_bracket_sequence: str = bracket_sequence.replace("()", "")
        if new_bracket_sequence == bracket_sequence:
            break
        if new_bracket_sequence == "":
            result = True
            break
        bracket_sequence = new_bracket_sequence

    return result


def main() -> None:
    bracket_sequence: str = input("Enter bracket sequence: ")
    print("The bracket sequence is correct") if bracket_sequence_correct(
        bracket_sequence) else print("The bracket sequence is not correct")


if __name__ == '__main__':
    main()
