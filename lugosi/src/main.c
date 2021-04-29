#include "callbacks.h"
#include "scene.h"
#include "camera.h"
#include <GL/glut.h>
#include <stdio.h>

void init_opengl()
{
    glShadeModel(GL_SMOOTH);

    glEnable(GL_NORMALIZE);
    glEnable(GL_AUTO_NORMAL);

    glClearColor(0.1, 0.1, 0.1, 1.0);

    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
	
	gluLookAt(
        1.0, 1.0, 2.0, // eye
        0.0, 0.0, 0.0, // look at
        0.0, 0.0, 1.0  // up
    );

    glEnable(GL_DEPTH_TEST);

    glClearDepth(1.0);

    glEnable(GL_TEXTURE_2D);

    glEnable(GL_LIGHTING);
    glEnable(GL_LIGHT0);
}

void set_callbacks()
{
    glutDisplayFunc(display);
    glutReshapeFunc(reshape);
    glutMouseFunc(mouse);
    glutMotionFunc(motion);
    glutKeyboardFunc(keyboard);
    glutKeyboardUpFunc(keyboard_up);
    glutIdleFunc(idle);
}

int main(int argc, char* argv[])
{	
	int window;
	rotateX = 0.0;
    rotateY = 0.0;

    glutInit(&argc, argv);

    glutInitWindowSize(1024, 1024);
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH);
	
	window = glutCreateWindow("Scene with a camera");
    glutSetWindow(window);

    init_opengl();
    init_scene(&scene);
    init_camera(&camera);
	set_callbacks();

    glutMainLoop();
	
    return 0;
}