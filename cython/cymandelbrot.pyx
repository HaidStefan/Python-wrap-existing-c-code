# distutils: sources = ../c_reference/lib/mandelbrot.c ../c_reference/lib/my_complex.c
# distutils: include_dirs = ../c_reference/lib

cimport cmandelbrot

def mandelbrot_c():
    cmandelbrot.mandelbrot()
