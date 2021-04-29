#ifndef CAMERA_H
#define CAMERA_H

#include "scene.h"

typedef struct vec3
{
    float x;
    float y;
    float z;
} vec3;

typedef struct Camera
{
    struct vec3 position;
    struct vec3 rotation;
    struct vec3 speed;
} Camera;

Camera camera;
double rotateX;
double rotateY;

int is_preview_visible;

void init_camera(Camera* camera);

void update_camera(Camera* camera, double time);

void set_view(const Camera* camera);

void rotate_camera(Camera* camera, double horizontal, double vertical);

void set_camera_speed(Camera* camera, double speed);

void set_camera_side_speed(Camera* camera, double speed);

double degree_to_radian(double degree);

void show_texture_preview();

#endif