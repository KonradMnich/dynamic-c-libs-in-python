"""The script shows how to use c code in python.
The dynamic library my_dll_for_python.dll was created
uniquelly for demo purposes and is generally useless.
"""
import ctypes


if __name__ == "__main__":
    library_path = "my_dll_for_python.dll"
    my_library = ctypes.CDLL(library_path)

    # The simplestcall; no input, no output
    my_library.display_message()

    # Still simple message but with an integer input
    my_int_input = 3
    my_library.display_message_with_input(my_int_input)

    # Call that returns something
    first_int = 3
    second_int = 4
    integer_sum = my_library.add_ints(first_int, second_int)
    print(f"{first_int} + {second_int} = {integer_sum}")

    # Addition of doubles
    # Mind that if the inputs are anything else than int, it must be
    # explicitly told to the interpreter:
    first_double = ctypes.c_double(3.1)
    second_double = ctypes.c_double(4.3)
    # The output must also be explicitely defined
    my_library.add_doubles.restype = ctypes.c_double
    double_sum = my_library.add_doubles(first_double, second_double)
    print(f"{first_double} + {second_double} = {double_sum}")

    # Summation of an array
    # Steps to create a c-style array from the python array:
    # (I wish to knew a more straight forward way to do it)
    my_array = [11, 22, 33]
    NewArray = ctypes.c_double * len(my_array)
    my_c_array = NewArray(*my_array)
    my_library.sum_array.restype = ctypes.c_double
    array_sum = my_library.sum_array(my_c_array, len(my_array))
    print(f"sum({my_array}) = {array_sum}")

    # Raise the array to the power of 2
    my_array2 = [11, 22, 33]
    NewArray2 = ctypes.c_double * len(my_array2)
    my_c_array2 = NewArray2(*my_array2)
    my_library.square_array(my_c_array2, len(my_array2))
    # Here the array was passed to the function as a reference
    # so it's oryginal values were modified
    print(f"({my_array})^2 = {[my_c_array2[i] for i in range(len(my_array2))]}")
