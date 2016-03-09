"""
Archivo para probar el uso de librerias en C desde Python
"""

import ctypes as C

libr = C.CDLL('./pruebalib.so')

a = 5
b = 8
c = 0

print(libr.add_int(a,b))
libr.add_float.restype = C.c_float
libr.add_float.argtypes = [C.c_float,C.c_float]
print(libr.add_float(a,b))
ab = C.c_int(a)
bb = C.c_int(b)
cb = C.c_int(c)
libr.add_int_ref(C.byref(ab),C.byref(bb),C.byref(cb))
print(cb.value)

ab = C.c_float(a)
bb = C.c_float(b)
cb = C.c_float(c)
libr.add_float_ref(C.byref(ab),C.byref(bb),C.byref(cb))
print(cb.value)

# Prueba arrays

arr1 = (C.c_int * 5) (1,2,3,4,5)
arr2 = (C.c_int * 5) (1,3,5,7,9)
arr3 = (C.c_int * 5) ()

libr.add_int_array(C.byref(arr1),C.byref(arr2),C.byref(arr3),5)
for i in range(5):
    print(arr3[i])

ar1 = (C.c_float * 5) (1.0,2.0,3.0,4.0,5.0)
ar2 = (C.c_float * 5) (1.0,3.0,5.0,7.0,9.0)
ar3 = (C.c_float * 5) ()

print(libr.dot_product(C.byref(ar1),C.byref(ar2),5))
