#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    for i in range(list_length):
        try:
            value_1 = my_list_1[i] if i < len(my_list_1) else 0
            value_2 = my_list_2[i] if i < len(my_list_2) else 0

            if not (isinstance(value_1, (int, float)) and isinstance(value_2, (int, float))):
                raise TypeError("wrong type")

            if value_2 == 0:
                raise ZeroDivisionError("division by 0")

            result = value_1 / value_2
            result_list.append(result)

        except TypeError as e:
            print(e)
            result_list.append(0)

        except ZeroDivisionError as e:
            print(e)
            result_list.append(0)

        except IndexError:
            print("out of range")
            result_list.append(0)

        finally:
            pass

    return result_list
