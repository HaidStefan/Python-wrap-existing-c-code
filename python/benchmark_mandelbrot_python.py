# Baseline code

import numpy as np
import timeit


def mandelbrot(width, height):
    # Create an array of bytes to store pixel values
    p = np.zeros((width, height), dtype=np.uint8)

    f = open('mandelbrot_python.pgm', 'w')
    f.write('P5\n{:d} {:d}\n255\n'.format(width, height))

    # Calculate pixel values
    for y in range(height):
        for x in range(width):
            # Initialize complex values from c and z for next iterative pixel value condition
            c = (-2.0 + x * 4.0 / width) + (2.0 - y * 4.0 / height) * (0 + 1j)
            z = 0 + 0j
            # Iterate complex function while darkening pixel
            px = 255
            while px >= 10 and abs(z) < 4.0:
                z = z * z + c
                px -= 10
            # Store latest pixel value in array
            p[y][x] = px

    # Write the byte array to the output file
    # f.write(bytearray(p))
    p.tofile(f)
    f.close()


if __name__ == '__main__':
    number_of_times = 3

    py_tot = timeit.timeit("mandelbrot(4000, 4000)",
                           setup="from mandelbrot_base import mandelbrot",
                           number=number_of_times)

    py_avg = py_tot / number_of_times
    print("Python average time:  {0:.6g}".format(py_avg))
