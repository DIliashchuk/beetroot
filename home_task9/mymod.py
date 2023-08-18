def count_lines(name):
    with open(name, 'r') as file:
        lines = file.readlines()
        return len(lines)


def count_chars(name):
    with open(name, 'r') as file:
        content = file.read()
        return len(content)


def test(name):
    line_count = count_lines(name)
    char_count = count_chars(name)

    print(f"Number of lines in the file: {line_count}")
    print(f"Number of characters in the file: {char_count}")


# Example usage
filename = 'Kotlyarevskii_Eneida.txt'
test(filename)