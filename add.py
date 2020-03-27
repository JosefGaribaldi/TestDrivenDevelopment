def Add(numbers):
    if numbers == '':
        return 0
    else:
        if len(numbers) == 3:
            numbers = numbers.split(',')
            return int(numbers[0])+int(numbers[1])
        return int(numbers)

assert Add('') == 0
assert Add('1') == 1
assert Add('1,2') == 3