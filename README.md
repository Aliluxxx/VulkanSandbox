# VulkanSandbox
A sandbox to test Vulkan API in C++

## Download instructions
To clone the repository use the following git command:
`git clone --recursive https://github.com/Aliluxxx/VulkanSandbox VulkanSandbox`.

If the repository was cloned non-recursively previously, type `git submodule update --init` to clone the necessary submodules.

## Setup instructions
To check for the necessary tools, inside the `scripts` folder run the command `python Setup.py` (you must have [Python3](https://www.python.org/downloads/) installed on your machine).
The script will check if you have [CMake](https://cmake.org/download/) and the required [Vulkan SDK (1.4.335.0)](https://vulkan.lunarg.com/sdk/home) version installed. If not, it will automatically install them (on some operating systems, the process may require manual installation).
