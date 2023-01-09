#include <Python.h>

/**
 * print_python_list_info - prints all the python list info .
 * @p: PyObject .
 * Return: no return .
 */
void print_python_list_info(PyObject *p)
{
	long int siz, g;
	PyListObject *list;
	PyObject *item;

	siz = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", siz);

	list = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", list->allocated);

	for (g = 0; g < siz; g++)
	{
		item = PyList_GetItem(p, g);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
