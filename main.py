def count_fizz_buzz():
    return_array = []
    for i in range(1, 101):
        temp_string = ''
        temp_string += fb(i, 3, 'Fizz')
        temp_string += fb(i, 5, 'Buzz')
        if temp_string == '':
            return_array.append(str(i))
        else:
            return_array.append(temp_string)
    return return_array


# test condition if j is in i, and so return txt
def fb(i, j, txt):
    if (i % j == 0) or (str(j) in str(i)):
        return exception_fb(txt)
    return ''


# adapt txt variation
def exception_fb(p_string):
    return '... ' + p_string + ' ... '


if __name__ == '__main__':
    pprint(count_fizz_buzz())
