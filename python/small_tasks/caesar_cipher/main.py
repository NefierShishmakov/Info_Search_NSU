import io
import os.path


def language_correct(language: str) -> bool:
    return language == "Eng" or language == "Rus"


def get_alphabet_power(language: str) -> int:
    alphabet_dict = {
        "Eng": 26,
        "Rus": 33
    }

    return alphabet_dict[language]


def get_file_text(text_file_path: str) -> str:
    with open(text_file_path, 'r') as f:
        file_text: str = f.read()
    return file_text


def get_encrypted_text(file_text: str, alphabet_power: int, shift: int, dictionary: str, dictionary_upper: str) -> str:
    result_text = io.StringIO()
    for char in file_text:
        if dictionary.find(char) == -1 and dictionary_upper.find(char) == -1:
            result_text.write(char)
            continue
        char_idx: int = dictionary.index(char) if char.islower() else dictionary_upper.index(char)
        encrypted_char_idx: int = (char_idx + shift) % alphabet_power
        encrypted_char = dictionary[encrypted_char_idx] if char.islower() else dictionary_upper[encrypted_char_idx]
        result_text.write(encrypted_char)

    return result_text.getvalue()


def write_encrypted_text_to_file(encrypted_text: str) -> None:
    file_name: str = "encrypted_text.txt"
    with open(file_name, "w") as f:
        f.write(encrypted_text)


def main() -> None:
    text_file_path: str = input("Enter text file path: ")
    if not os.path.isfile(text_file_path):
        print(text_file_path + " is not a file")
        return

    try:
        shift = int(input("Enter shift: "))
    except ValueError:
        print("Shift must be a positive integer")
        return

    if shift < 0:
        print("Shift must be a positive integer")
        return

    language = input("Enter language - \"Eng\" or \"Rus\": ")
    if not language_correct(language):
        print("Language must be \"Eng\" or \"Rus\"")
        return

    file_text: str = get_file_text(text_file_path)
    alphabet_power: int = get_alphabet_power(language)
    if language == "Eng":
        dictionary, dictionary_upper = "abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    else:
        dictionary, dictionary_upper = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя", "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

    encrypted_text: str = get_encrypted_text(file_text, alphabet_power, shift, dictionary, dictionary_upper)
    write_encrypted_text_to_file(encrypted_text)


if __name__ == '__main__':
    main()
