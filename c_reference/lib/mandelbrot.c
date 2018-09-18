#include <stdio.h>
#include <windows.h>
#include <math.h>
#include "my_complex.h"
#include "mandelbrot.h"

unsigned char p[4000][4000];

void mandelbrot() {

	my_complex* c;
	my_complex* z;
	c = malloc(sizeof(my_complex));
	z = malloc(sizeof(my_complex));
	int width = 4000, height = 4000, x, y;
	unsigned char px;

	//Open output file
	FILE* f = fopen("mandelbrot_c.pgm", "w");
	fprintf(f, "P5\n%d %d\n255\n", width, height);

	//Calculate pixel values
	for (y = 0; y < height; ++y) {
		for (x = 0; x < width; ++x) {
			//Initialize complex values c and z for next iterative pixel value condition
			//c = (-2.0 + x * 4.0 / width) + (2.0 - y * 4.0 / height) * I;
			c->real = (-2.0 + x * 4.0 / width);
			c->imag = (2.0 - y * 4.0 / height);
			//z = 0;
			z->real = 0.0;
			z->imag = 0.0;

			//Iterate complex function while darkening pixel
			px = 255;
			while (px >= 10 && c_abs(z) < 4.0) {
				//z = z * z + c;
				pow2(z);
				z->real = z->real + c->real;
				z->imag = z->imag + c->imag;

				px -= 10;
			}
			//Store latest pixel value in byte array
			p[y][x] = px;
		}
	}

	free(c);
	free(z);

	fwrite(p, 1, width * height, f);
	fclose(f);
}
