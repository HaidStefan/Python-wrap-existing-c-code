/*
 ============================================================================
 Name        : Mandelbrot_benchmark.c
 Author      : Stefan Haid
 Version     :
 Description : Main file to time the mandelbrot algorithm in c
 ============================================================================
 */

#include <stdio.h>
#include <windows.h>
#include <math.h>

#include "lib/mandelbrot.h"

int main(void) {

	LARGE_INTEGER frequency;
	LARGE_INTEGER t1, t2;
	double time;
	QueryPerformanceFrequency(&frequency);

	QueryPerformanceCounter(&t1); //start timer
	mandelbrot();
	QueryPerformanceCounter(&t2); //stop timer

	// compute and print the elapsed time in ns
	time = (t2.QuadPart - t1.QuadPart) * 1e9 / frequency.QuadPart;
	printf("Time: %f ns", time);
}

