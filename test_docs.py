import doctest
import math

def triangleArea(b,h):

    '''
    Find the triangle area

    >>> triangleArea(3,6)
    'The triangle area is 9.0'
    
    >>> triangleArea(4,4)
    'The triangle area is 8.0'

    >>> triangleArea(9,2)
    'The triangle area is 9.0'

    '''

    return f'The triangle area is {(b*h)/2}'


def square_root(number_list):

    '''

    return the list with the square root of the numbers given

    >>> l = []
    >>> for i in [4, 9, 16]:
    ...     l.append(i)
    >>> square_root(l)
    [2.0, 3.0, 4.0]

    >>> l = []
    >>> for i in [4, 9, -16]:
    ...     l.append(i)
    >>> square_root(l)
    Traceback (most recent call last):
        ...
    ValueError: math domain error


    '''

    return [math.sqrt(n) for n in number_list]

# print(square_root([4, 9, -16]))
doctest.testmod()