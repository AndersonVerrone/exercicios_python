def corresponding_parenthesis(txt: str):
    open = txt.count('(')
    close = txt.count(')')
    difference = open - close

    if difference > 0:
        return '(' * difference
    elif difference < 0:
        return ')' * (difference * -1)

    return ''


print(corresponding_parenthesis('))'))


def remove_more_than_two_repetitions(text: str):
    response = []
    response.append(text[0])
    response.append(text[1])

    for index, char in enumerate(text[2:], 2):
        if text[index - 1] != char or text[index - 2] != char:
            response.append(char)

    return ''.join(response)


text = "Ollloco meuuuu, taaa peegaando fogoo biiiiichooo"
text = remove_more_than_two_repetitions(text)
print(text)
