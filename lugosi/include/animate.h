#ifndef ANIMATE_H
#define ANIMATE_H

typedef struct Mouth{
	const float left;
	const float right;
	float top;
	float bottom;
}Mouth;

typedef struct Eyebrow{
	const float left;
	const float right;
	float top;
	float bottom;
}Eyebrow;

void update_mouth(Mouth* mouth, char mimic[]);

void update_eyebrow(Eyebrow* eyebrow, char mimic[]);

#endif