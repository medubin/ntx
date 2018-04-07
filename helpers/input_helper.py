def is_title_character(input):
    if len(input) != 1:
        return False
    return (
        input.isalpha() or
        input.isdigit() or
        input in [' ', '-', '_', '.']
    )