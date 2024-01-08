#include <Python.h>
#include <stdio.h>

#ifdef __cplusplus
extern "C" {
#endif

void print_python_list_info(PyObject *p);

#ifdef __cplusplus
}
#endif

/**
 * print_python_list_info - prints basic info about Python lists
 * @p: pointer to a Python object (assumed to be a list)
 */
void print_python_list_info(PyObject *p)
{
    int size, i;
    PyListObject *list;

    size = PyList_Size(p);
    list = (PyListObject *)p;

    printf("[*] Size of the Python List = %d\n", size);
    printf("[*] Allocated = %d\n", (int)list->allocated);

    for (i = 0; i < size; i++)
    {
        printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
    }
}

int main(void)
{
    PyObject *libPyList = PyCapsule_Import("libPyList", 0);
    if (libPyList == NULL)
        return -1;

    Py_Initialize();

    // Code number 1
    PyObject *list1 = PyList_New(0);
    PyList_Append(list1, PyUnicode_FromString("hello"));
    PyList_Append(list1, PyUnicode_FromString("World"));

    ((void (*)(PyObject *))PyCapsule_GetPointer(libPyList, "print_python_list_info"))(list1);

    // Cleanup
    Py_DECREF(list1);

    // Code number 2
    PyObject *list2 = PyList_New(0);
    PyList_Append(list2, PyUnicode_FromString("hello"));
    PyList_Append(list2, PyUnicode_FromString("World"));

    ((void (*)(PyObject *))PyCapsule_GetPointer(libPyList, "print_python_list_info"))(list2);

    // Cleanup
    Py_DECREF(list2);

    Py_Finalize();

    return 0;
}
