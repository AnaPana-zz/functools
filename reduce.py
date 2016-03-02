from functools import reduce


def calculate_sum(lst):
    """
    Simple 'reduce' example.
    """
    # lst=[1,2,3,4,5]
    # ((((1+2)+3)+4)+5)
    sum = reduce(lambda x,y: x+y, lst)
    return sum


def flatten_list(*lists):
    """
    Turn ([1, 2, 3], [4, 5], [6, 7, 8]) into [1, 2, 3, 4, 5, 6, 7, 8]
    *lists -> read all positional arguments and save them into the tuple
    """
    # Last argument is initializer
    # If the optional initializer is present, it is placed before the items of
    # the sequence in the calculation, and serves as a default when the sequence
    # is empty.
    lst = reduce(list.__add__, lists, [])
    return lst


def list_of_digitst_to_number(lst):
    """
    Turn [1, 2, 3, 4, 5, 6, 7, 8] into 12345678

    1*10+2=12
    12*10+3=123
    123*10+4=1234
    ...
    """
    n = reduce(lambda a,d: 10*a+d, lst, 0)
    return n


if __name__ == '__main__':
    print(calculate_sum([1,2,3,4,5]))
    print(flatten_list([1,2,3], [4,5,6], [7,8,9]))
    print(list_of_digitst_to_number([1,2,3,4]))
