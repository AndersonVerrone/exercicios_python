def text_to_array(text: str):
    return text.split()


print(text_to_array("I love arrays they are my favorite"))


def sum(num_1: str, num_2: str):
    return str(int(num_1) + int(num_2))


print(sum("4", "5"))


def say_hello(name: str):
    return f'Hello, {name} how are you doing today?'


print(say_hello('Anderson'))


def remove(text: str):
    if text[-1] == "!":
        text = text[:-1]
    return text


print(remove('!!Hi!'))
print(remove('Hi'))


def reverse_txt(text: str):
    text_array = text.split()
    text_array.reverse()
    return ' '.join(text_array)


print(reverse_txt("The greatest victory is that which requires no battle"))


def repeat_str(n: int, text: str):
    new_str = ''
    for x in range(n):
        new_str = new_str + text
    return new_str


print(repeat_str(5, "Hello"))
