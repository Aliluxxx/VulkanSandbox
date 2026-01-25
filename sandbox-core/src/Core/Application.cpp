#include <iostream>

#include <GLFW/glfw3.h>

void Test() {

	std::cout << "Hello Vulkan\n";

	glfwInit();

	glfwWindowHint(GLFW_CLIENT_API, GLFW_NO_API);
	GLFWwindow* window = glfwCreateWindow(800, 600, "Vulkan", nullptr, nullptr);

	while (!glfwWindowShouldClose(window)) {

		glfwPollEvents();
	}

	glfwDestroyWindow(window);

	glfwTerminate();
}
