#include <stdio.h>
#include <math.h>
#include "my_complex.h"

void pow2(my_complex* c1) {
	double temp = c1->real * c1->real - c1->imag * c1->imag;
	c1->imag = 2 * (c1->real * c1->imag);
	c1->real = temp;
}

double c_abs(my_complex* c1) {
	return sqrt(c1->real * c1->real + c1->imag * c1->imag);
}
