all:
	gcc -g -Iinclude/ src/main.c src/camera.c src/model.c src/callbacks.c src/scene.c src/load.c src/animate.c -lSOIL -lobj -lopengl32 -lglu32 -lglut32 -lm -o lugosi.exe
linux:
	gcc -g -Iinclude/ src/main.c src/camera.c src/model.c src/callbacks.c src/scene.c src/load.c src/animate.c -lSOIL -lobj -lGL -lGLU -lglut -lm -o lugosi