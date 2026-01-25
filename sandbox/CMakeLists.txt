cmake_minimum_required(VERSION 3.29)

file(GLOB_RECURSE SOURCES "src/*.cpp")
file(GLOB_RECURSE HEADERS "src/*.h")

add_executable("sandbox")

target_sources("sandbox"
	PRIVATE
	${HEADERS}
	${SOURCES}
)

target_include_directories("sandbox"
	PRIVATE
	${CMAKE_CURRENT_SOURCE_DIR}/src
	${CMAKE_SOURCE_DIR}/sandbox-core/src
	${VULKAN_INCLUDE_DIR}
)

target_link_libraries("sandbox"
	PRIVATE
	"sandbox-core"
	$<$<CONFIG:Debug>:${VULKAN_LIB_DIRS_DEBUG}>
	$<$<CONFIG:Release>:${VULKAN_LIB_DIRS_RELEASE}>
	$<$<CONFIG:Dist>:${VULKAN_LIB_DIRS_RELEASE}>
)

set_configurations_fn("sandbox")
set_output_dirs_fn("sandbox")
