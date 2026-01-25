cmake_minimum_required(VERSION 3.29)

set_property(GLOBAL PROPERTY USE_FOLDERS ON)

project(Sandbox VERSION 1.0 LANGUAGES CXX)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

set(CMAKE_CONFIGURATION_TYPES "Debug;Release;Dist" CACHE STRING "" FORCE)

set(CMAKE_EXE_LINKER_FLAGS_DIST "" CACHE STRING "" FORCE)
set(CMAKE_SHARED_LINKER_FLAGS_DIST "" CACHE STRING "" FORCE)
set(CMAKE_STATIC_LINKER_FLAGS_DIST "" CACHE STRING "" FORCE)

set(OUTPUT_DIR "$<CONFIG>")

function(set_configurations_fn target)
	target_compile_options(${target} PRIVATE
		# GCC / Clang
		$<$<AND:$<CONFIG:Debug>,$<NOT:$<CXX_COMPILER_ID:MSVC>>>:-O0 -g>
		$<$<AND:$<CONFIG:Release>,$<NOT:$<CXX_COMPILER_ID:MSVC>>>:-O2 -g>
		$<$<AND:$<CONFIG:Dist>,$<NOT:$<CXX_COMPILER_ID:MSVC>>>:-O3 -DNDEBUG>

		# MSVC
		$<$<AND:$<CONFIG:Debug>,$<CXX_COMPILER_ID:MSVC>>:/Od /Zi>
		$<$<AND:$<CONFIG:Release>,$<CXX_COMPILER_ID:MSVC>>:/O2 /Zi>
		$<$<AND:$<CONFIG:Dist>,$<CXX_COMPILER_ID:MSVC>>:/O2 /DNDEBUG>
	)
endfunction()

function(set_output_dirs_fn target)
	set_target_properties(${target} PROPERTIES
		RUNTIME_OUTPUT_DIRECTORY "$<BUILD_INTERFACE:${CMAKE_BINARY_DIR}/bin/${OUTPUT_DIR}>"
		LIBRARY_OUTPUT_DIRECTORY "$<BUILD_INTERFACE:${CMAKE_BINARY_DIR}/bin/${OUTPUT_DIR}>"
		ARCHIVE_OUTPUT_DIRECTORY "$<BUILD_INTERFACE:${CMAKE_BINARY_DIR}/bin/${OUTPUT_DIR}>"
	)
endfunction()

find_package(Vulkan REQUIRED)
message(STATUS "Vulkan include dirs: ${Vulkan_INCLUDE_DIRS}")
message(STATUS "Vulkan libraries: ${Vulkan_LIBRARIES}")

set(VULKAN_INCLUDE_DIR ${Vulkan_INCLUDE_DIRS})
get_filename_component(VULKAN_LIB_DIR ${Vulkan_LIBRARIES} DIRECTORY)

set(VULKAN_LIB_DIRS_DEBUG
	"${VULKAN_LIB_DIR}/vulkan-1.lib"
	"${VULKAN_LIB_DIR}/shaderc_sharedd.lib"
	"${VULKAN_LIB_DIR}/spirv-cross-cored.lib"
	"${VULKAN_LIB_DIR}/spirv-cross-glsld.lib"
	"${VULKAN_LIB_DIR}/SPIRV-Toolsd.lib"
)

set(VULKAN_LIB_DIRS_RELEASE
	"${VULKAN_LIB_DIR}/vulkan-1.lib"
	"${VULKAN_LIB_DIR}/shaderc_shared.lib"
	"${VULKAN_LIB_DIR}/spirv-cross-core.lib"
	"${VULKAN_LIB_DIR}/spirv-cross-glsl.lib"
	"${VULKAN_LIB_DIR}/SPIRV-Tools.lib"
)

add_subdirectory("sandbox")
add_subdirectory("sandbox-core")

set_property(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR} PROPERTY VS_STARTUP_PROJECT "sandbox")
