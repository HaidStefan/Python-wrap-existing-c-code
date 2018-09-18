# Wrap existing c-code for python

This is a sample project that wrap some functions from  existing c-libraries.
Cython, swig and cffi have been used to  build the wrappers.
<br/><br/>A benchmark and a summary has been added to compare the wrappers.


## Technologies
### Cython
Wrapping existing c-libraries is one of the main uses for cython. The way to do this, is
by using the external declarations of the variables and functions that should be wrapped.
Cython has an entire compiler, that can build a cython module, that can be imported and called from any python code.


### CFFI
For calling a C-library from Python cffi is recommended a lot because it is really simple to use.
It is a alternative to ctypes, with the advantage that it doesn't require non-Python glue-code for the binding.

CFFI is a foreign function call library (API mode), but it can also be used to compile and build a module from c files (ABI mode).
The ABI mode accesses libraries at the binary level, whereas the faster API mode accesses them with a C compiler.
In compatibility, the ABI mode has an advantage over the API mode as it doesn't require any pre-compilation.
CFFI offers for both, API and ABI an "in-line" and "out-of-line" mode. In the in-line mode, everything is set up,
when the python code is imported. At "out-of-line" the production of the module is precompiled and separated from the usage.


### SWIG
SWIG is a interface compiler that is able to connect higher programming languages like
Pyhton, PHP, JavaScript, Java, C# and a lot of other languages with existing C/C++ code. To do this, you need to write some files for
the binding that includes the function and variable definitions of the C/C++ header files.


<br/>

## Benchmark

### Mandelbrot algorithm

For the comparison, the average time of 100 executions have been used. The runtime cython and swig is even faster then c, because it was
compiled with a 64bit compiler. For only 100 function calls the difference is not really big between those tools.
(beside pythong ofc)

| Technology | Average time |
|------------|--------------|
| Python     | 36.391 s    |
| C          | 0.798 s     |
| CFFI_ABI   | 0.822 s     |
| CFFI_API   | 0.816 s     |
| SWIG       | 0.821 s     |
| Cython     | 0.812 s     |



### Primality test function

At this benchmark a simple is_prime(n) function has been used. The function is called 100.000.000 times, so we have a lot more function
calls, so the difference between the wrapping-technologies can be compared better. The difference comes from the overhead-code that was
generated from the tool for wrapping.

| Technology | Average time |
|------------|--------------|
| CFFI_ABI   | 155.796 ns   |
| SWIG       | 117.321 ns   |
| CFFI_API   | 113.371 ns   |
| Cython     | 59.576 ns    |

<br/> <br/>

## Things to consider beside speed

### Maintainability

### Compiler dependency

### Vulnerability to bugs

<br/>

## Summary

### CFFI
For wrapping existing c libraries CFFI is the most straight forward tool to use, as it is designed to interface with C.
If the generated code should be able to run on PyPy or CPython, CFFI has an advantage over Cython and SWIG, because these tools are
not fully compatible to them.
Another advantage of CFFI is, that it doesnt require any DSL (Domain Specific Language) to write the wrapper.

### SWIG
Swig has an advantage in compatibility because it also support a lot of other programming languages besides python. It can also be used
to interface C++ Code. One downside of SWIG is, that a lot of tutorials are outdated and deprecated. The problem in my opinion is, that
it is too flexible and can be used for a lot of different languages, but is not fully optimised for one thing.

### Cython
Cython is no binding generator tool like SWIG or CFFI. Cython is a programming language, and one use-case of Cython is to
bind Python with C. The advantage is that you have access to the code between C and Python.
A downside of Cython it requires to write a lot more files and code compared to automatic generator tools.


<br/>

## Resources used:
* [https://github.com/tleonhardt/Python_Interface_Cpp](https://github.com/tleonhardt/Python_Interface_Cpp)
* [https://batchloaf.wordpress.com/2016/02/03/c-or-python-comparison-of-execution-time-for-mandelbrot-image-generation/](https://batchloaf.wordpress.com/2016/02/03/c-or-python-comparison-of-execution-time-for-mandelbrot-image-generation/)
