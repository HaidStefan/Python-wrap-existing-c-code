
import timeit

if __name__ == '__main__':
    number_of_times = 10000000

    cython_tot = timeit.timeit("cylibrary.is_prime(7659921)",
                             setup="""import cylibrary""",
                             number=number_of_times)

cython_avg = cython_tot / number_of_times

print("cython average time:  {0:.9g}".format(cython_avg))

