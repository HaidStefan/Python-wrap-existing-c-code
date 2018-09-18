
import timeit

if __name__ == '__main__':
    number_of_times = 150

    cython_tot = timeit.timeit("cymandelbrot.mandelbrot_c()",
                             setup="""import cymandelbrot""",
                             number=number_of_times)

cython_avg = cython_tot / number_of_times

print("cython average time:  {0:.6g}".format(cython_avg))

