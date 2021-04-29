#include "animate.h"

#define NUM_POINTS 10

void update_mouth(Mouth* mouth, char mimic[])
{
	
}

void update_eyebrow(Eyebrow* eyebrow, char mimic[])
{

}

int point_localization(float x)
{
	int i = 0;
	int k = 0;
	int l = NUM_POINTS - 1;
	if (x == X[l]){
		i = l - 1;
	}
	while ((l - 1) > 1):
		k = (i + l) / 2;
		if (x < X[k]){
			l = k;
		}
		else if (x == X[k]){
			return k;
		}
		else{
			i = k;
		}
	return i;
}

float linear_interpolation(float x)
{
	int i = point_localization(x);
	return Y[i] + (Y[i+1] - Y[i]) / (X[i+1] - X[i]) * (x - X[i]);
}


			
	