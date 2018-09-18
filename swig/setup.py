from distutils.core import setup, Extension

name = "mandelbrot"
version = "0.1"

setup(name=name, version=version,
      ext_modules=[Extension(name='_{}'.format(name),
                             sources=["mandelbrot.i", "../c_reference/lib/mandelbrot.c",
                                      "../c_reference/lib/my_complex.c", "../c_reference/lib/prime.c"],
                             include_dirs=[],
                             swig_opts=[])
                   ])
