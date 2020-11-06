from main import count_fizz_buzz, exception_fb, fb


def test_exception_fb():
    assert exception_fb('test') == '... test ... '


def test_fb():
    assert fb(2, 2, 'test') == exception_fb('test')
    assert fb(6, 5, 'test') == ''
    assert fb(14, 4, 'test') == exception_fb('test')


def test_count_fizz_buzz():
    assert count_fizz_buzz()[0] == '1'
    assert count_fizz_buzz()[2] == '... Fizz ... '
    assert count_fizz_buzz()[4] == '... Buzz ... '
    assert count_fizz_buzz()[12] == '... Fizz ... '
    assert count_fizz_buzz()[14] == '... Fizz ... ... Buzz ... '
    assert count_fizz_buzz()[50] == '... Fizz ... ... Buzz ... '
    assert count_fizz_buzz()[54] == '... Buzz ... '
    assert count_fizz_buzz()[99] == '... Buzz ... '


def green_traffic_light_pattern():
    return 'All tests passed'


if __name__ == '__main__':
    test_exception_fb()
    test_fb()
    test_count_fizz_buzz()
    print(green_traffic_light_pattern())

