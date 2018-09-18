import timeit

if __name__ == '__main__':
    number_of_times = 15

    cffi_tot = timeit.timeit("lib.mandelbrot()",
                             setup="""from _example import ffi, lib""",
                             number=number_of_times)

    cffi_avg = cffi_tot / number_of_times

    print("cffi api average time:  {0:.10g}".format(cffi_avg))
