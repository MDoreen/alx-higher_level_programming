#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0

    for item in my_list:
        if i > x:
            break
        try:
            i += 1
            if i < x:
                print(item, end='')
            elif i == x:
                print(item)
                break
        except (RuntimeError, TypeError, NameError) as err:
            print(f"Unexpected {err=}, {type(err)=}")

    return (i)
