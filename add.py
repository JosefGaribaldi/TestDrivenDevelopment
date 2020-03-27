def Add(numbers):
    if numbers == '':
        return 0
    else:
        total = 0
        string = 'Negatives not allowed:'
        numbers = numbers.replace('\n', ',')
        numbers = numbers.split(',')
        for letter in numbers:
            if int(letter)< 1000:
                if int(letter) < 0:
                    if string != 'Negatives not allowed:':
                        string+= ','
                    string += letter
                total += int(letter)
        if string != 'Negatives not allowed:':
            return string
        return total

assert Add('') == 0
assert Add('1') == 1
assert Add('1,2') == 3
assert Add('1,2,3,4,5') == 15
assert Add('10,2,5,22,1,1') == 41
assert Add('1\n2,3') == 6
assert Add('1001,2') == 2
assert Add('-1,2') == 'Negatives not allowed:-1'