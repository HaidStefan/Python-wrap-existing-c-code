from cffi import FFI
import os

ffibuilder = FFI()

ffibuilder.set_source("_example",
                      r""" //passed to the real C compiler
                           //It contains the implementation of the things tht are declared in cdef()
                          
                      #include "../c_reference/lib/prime.h"
                      #include "../c_reference/lib/mandelbrot.h"    
                                                                                  
                      """,
                      sources=["../c_reference/lib/prime.c",
                               "../c_reference/lib/my_complex.c",
                               "../c_reference/lib/mandelbrot.c"])


ffibuilder.cdef("""
    //declarations that are shared between Python and C
    int is_prime(long num);
    void mandelbrot(void);
""")

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
