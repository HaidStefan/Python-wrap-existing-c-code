### Commands to build the shared library:

```
gcc -c ..\c_reference\lib\mandelbrot.c -o mandel.o
gcc -c ..\c_reference\lib\my_complex.c -o my_complex.o
gcc -shared -o libmandel.so mandel.o my_complex.o
```