import cffi
import os
import timeit

ffi = cffi.FFI()
ffi.cdef('int is_prime(long num);')
lib = ffi.dlopen(os.path.join('.', 'lib.so'));

if __name__ == '__main__':
    number_of_times = 10000000

    cffi_tot = timeit.timeit("lib.is_prime(7659921)",
                             setup="""import cffi; import os; ffi = cffi.FFI(); ffi.cdef('int is_prime(long num);'); lib = ffi.dlopen(os.path.join('.', 'lib.so'))""",
                             number=number_of_times)

    cffi_avg = cffi_tot / number_of_times

    print("cffi abi average time:  {0:.10g}".format(cffi_avg))