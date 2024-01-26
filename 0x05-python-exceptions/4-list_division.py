#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    i = 0
    while i < list_length:
        try:
            result_list.append(my_list_1[i] / my_list_2[i])
        except IndexError:
            print('out of range')
            result_list.append(0)
        except ZeroDivisionError:
            print('division by 0')
            result_list.append(0)
        except TypeError:
            print('wrong type')
            result_list.append(0)
        finally:
            pass
        i += 1
    return result_list
