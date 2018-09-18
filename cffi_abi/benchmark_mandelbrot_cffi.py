import timeit

if __name__ == '__main__':
    number_of_times = 30

    cffi_tot = timeit.timeit("lib.mandelbrot()",
                             setup="""import cffi; import os; ffi = cffi.FFI(); ffi.cdef('void mandelbrot(void);'); lib = ffi.dlopen(os.path.join('.', 'libmandel.so'))""",
                             number=number_of_times)

cffi_avg = cffi_tot / number_of_times

print("cffi average time:  {0:.7g}".format(cffi_avg))
