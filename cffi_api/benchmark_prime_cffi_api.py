import timeit

if __name__ == '__main__':
    number_of_times = 10000000

    cffi_tot = timeit.timeit("lib.is_prime(7659921)",
                             setup="""from _example import ffi, lib""",
                             number=number_of_times)

    cffi_avg = cffi_tot / number_of_times

    print("cffi api average time:  {0:.10g}".format(cffi_avg))
