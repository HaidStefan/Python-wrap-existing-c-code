from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

setup(
    #name="mandelbrot",
    #ext_modules=cythonize([Extension("cymandelbrot", ["cymandelbrot.pyx"])])
    name="library",
    ext_modules=cythonize([Extension("cylibrary", ["cylibrary.pyx"])])
)
