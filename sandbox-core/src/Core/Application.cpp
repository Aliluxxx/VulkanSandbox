#include <GLFW/glfw3.h>

void Test() {

	sb::Log::Init();

	SB_INFO("Hello Vulkan");

	glfwInit();

	glfwWindowHint(GLFW_CLIENT_API, GLFW_NO_API);
	GLFWwindow* window = glfwCreateWindow(800, 600, "Vulkan", nullptr, nullptr);

	while (!glfwWindowShouldClose(window)) {

		glfwPollEvents();
	}

	glfwDestroyWindow(window);

	glfwTerminate();
}
