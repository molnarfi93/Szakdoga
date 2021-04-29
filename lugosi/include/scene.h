#ifndef SCENE_H
#define SCENE_H

#include "camera.h"
#include "model.h"
#include <GL/glut.h>

typedef struct Color
{
    float red;
    float green;
    float blue;
} Color;

typedef struct Material
{
    struct Color ambient; 
    struct Color diffuse; 
    struct Color specular; 
    float shininess;
} Material;

typedef struct Scene
{
    Model lugosi;
    Material material;
    GLuint texture_id;
} Scene;

Scene scene;

void init_scene(Scene* scene);

void set_lighting();

void set_material(const Material* material);

void draw_scene(const Scene* scene);

void draw_origin();

void draw_model(const Model* model);

void draw_triangles(const Model* model);

#endif