/* mandelbrot.i */
 %module mandelbrot
 %{
 /* Includes the header in the wrapper code */
 #include "../c_reference/lib/mandelbrot.h"
 #include "../c_reference/lib/library.h"
 %}

/* Parse the header file to generate wrappers */
 %include "../c_reference/lib/mandelbrot.h"
 %include "../c_reference/lib/library.h"