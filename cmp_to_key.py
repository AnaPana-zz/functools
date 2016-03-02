from functools import cmp_to_key


# Applicable to sorted(), min(), max(), heapq.ArithmeticErrornsmallest(),
# itertools.groupby() ...


tuple_to_sort = (
    ('bla', 3),
    ('aaa', 1),
    ('foo', 2),
    ('boo', 2)
)


print(sorted(tuple_to_sort, key=lambda x: x[0]))
# [('aaa', 1), ('bla', 3), ('boo', 2), ('foo', 2)]

print(sorted(tuple_to_sort, key=lambda x: x[1]))
# [('aaa', 1), ('foo', 2), ('boo', 2), ('bla', 3)]


def my_compare(x, y):
    """
    I want my results to be [2, 2, ..., everything else]
    """
    if x[1] == 2 or y[1] == 2:
        return -1


print(sorted(tuple_to_sort, key=cmp_to_key(my_compare)))
# [('boo', 2), ('foo', 2), ('aaa', 1), ('bla', 3)]
