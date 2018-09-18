#ifndef MY_COMPLEX_LIB
#define MY_COMPLEX_LIB

#pragma once
typedef struct my_complex {
	double real;
	double imag;
} my_complex;

void pow2(my_complex* c1);
double c_abs(my_complex* c1);

#endif
