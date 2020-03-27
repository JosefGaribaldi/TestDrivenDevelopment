def Add(numbers):
    if numbers == '':
        return 0
    else:
        total = 0
        numbers = numbers.split(',')
        for letter in numbers:
            if letter.isdigit():
                total += int(letter)
        return total

assert Add('') == 0
assert Add('1') == 1
assert Add('1,2') == 3
assert Add('1,2,3,4,5') == 15
assert Add('10,2,5,22,1,1') == 41