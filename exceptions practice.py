#x= 11
#if x > 5:
    #raise Exception('x should not exceed 5. The value of x was {}'.format(x))


def modify_x():
    assert x <= 5, 'x should not exceed 5. The value of x was {}'.format(x)
    print('There was no Assertion Error')

try:
    x = 4
    modify_x()
except AssertionError as error:
    print(error)
    print('modify_x() function was not successfully executed')