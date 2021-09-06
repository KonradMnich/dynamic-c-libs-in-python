// my_dll_for_python.h contains prototypes of functions that can be used via python ctypes.
// The library was designed uniquely to demonstrate how the c code
// contained in a dll file can be used in the python code.
//
// This file is included in the repository only for information, it is not required to run
// the program.
//
// The library is build on the example provided by Microsoft (last accessed on 2021-09-06):
// https://docs.microsoft.com/en-us/cpp/build/walkthrough-creating-and-using-a-dynamic-link-library-cpp?view=msvc-160
#pragma once

#ifdef MYDLLFORPYTHON_EXPORTS

#define MYLIBRARY_API __declspec(dllexport)
#else
#define MYLIBRARY_API __declspec(dllimport)
#endif

// Only displays a message
extern "C" MYLIBRARY_API void display_message();

// Displays a message with a given input a
extern "C" MYLIBRARY_API void display_message_with_input(int a);

// Returns a sum of two ints
extern "C" MYLIBRARY_API int add_ints(int a, int b);

// Returns a sum of two doubles
extern "C" MYLIBRARY_API double add_doubles(double a, double b);

// Returns a sum of an array of doubles
extern "C" MYLIBRARY_API double sum_array(double a[], int length);

// Raises all the elements of the passed array to the power of two
extern "C" MYLIBRARY_API void square_array(double a[], int length);
