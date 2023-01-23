#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """Divides element by element from two lists.

    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The number of elements to divide.

    Returns:
        A new list (length = list_length) with all divisions.
    """
    newlist = []
    for x in range(list_length):
        try:
            newlist.append(my_list_1[x] / my_list_2[x])
        except TypeError:
            print("wrong type")
            newlist.append(0)
            continue
        except ArithmeticError:
            print("division by 0")
            newlist.append(0)
            continue
        except IndexError:
            print("out of range")
            newlist.append(0)
            continue
        finally:
            pass
    return newlist
