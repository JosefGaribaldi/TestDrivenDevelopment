def Add(numbers):
    if numbers == '':
        return 0
    else:
        if numbers.isdigit():
            return int(numbers)

assert Add('') == 0
assert Add('1') == 1