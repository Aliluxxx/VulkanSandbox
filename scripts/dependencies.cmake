# Include dirs
set(SANDBOX_INCLUDE_DIRS
	${CMAKE_CURRENT_SOURCE_DIR}/src
	${CMAKE_SOURCE_DIR}/sandbox-core/src
)

# Library dirs
set(SANDBOX_LIB_DIRS
	"sandbox-core"
)

# Submodule libraries
list(APPEND SANDBOX_INCLUDE_DIRS
	${CMAKE_SOURCE_DIR}/sandbox-core/libs/glfw/include
	${CMAKE_SOURCE_DIR}/sandbox-core/libs/glm
)
list(APPEND SANDBOX_LIB_DIRS
	glfw
)

# Vulkan dependencies
find_package(Vulkan REQUIRED)
message(STATUS "Vulkan include dirs: ${Vulkan_INCLUDE_DIRS}")
message(STATUS "Vulkan libraries: ${Vulkan_LIBRARIES}")

set(VULKAN_INCLUDE_DIR ${Vulkan_INCLUDE_DIRS})
list(APPEND SANDBOX_INCLUDE_DIRS ${VULKAN_INCLUDE_DIR})
get_filename_component(VULKAN_LIB_DIR ${Vulkan_LIBRARIES} DIRECTORY)
list(APPEND SANDBOX_LIB_DIRS "${Vulkan_LIBRARIES}")

set(VULKAN_LIB_DIRS_DEBUG
	"${VULKAN_LIB_DIR}/shaderc_sharedd.lib"
	"${VULKAN_LIB_DIR}/spirv-cross-cored.lib"
	"${VULKAN_LIB_DIR}/spirv-cross-glsld.lib"
	"${VULKAN_LIB_DIR}/SPIRV-Toolsd.lib"
)

set(VULKAN_LIB_DIRS_RELEASE
	"${VULKAN_LIB_DIR}/shaderc_shared.lib"
	"${VULKAN_LIB_DIR}/spirv-cross-core.lib"
	"${VULKAN_LIB_DIR}/spirv-cross-glsl.lib"
	"${VULKAN_LIB_DIR}/SPIRV-Tools.lib"
)
