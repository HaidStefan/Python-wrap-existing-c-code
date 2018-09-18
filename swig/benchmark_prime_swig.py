import mandelbrot
import timeit

if __name__ == '__main__':
    number_of_times = 10000000

    swig_tot = timeit.timeit("mandelbrot.is_prime(7659921)",
                             setup="""import mandelbrot""",
                             number=number_of_times)

swig_avg = swig_tot / number_of_times

print("swig average time:  {0:.6g}".format(swig_avg))

mandelbrot.mandelbrot()

