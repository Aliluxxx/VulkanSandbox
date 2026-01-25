cmake_minimum_required(VERSION 3.29)

file(GLOB_RECURSE SOURCES "src/*.cpp")
file(GLOB_RECURSE HEADERS "src/*.h")

add_library("sandbox-core" STATIC)

target_sources("sandbox-core"
	PRIVATE
		${HEADERS}
		${SOURCES}
)

target_include_directories("sandbox-core"
	PRIVATE
	${SANDBOX_INCLUDE_DIRS}
)

set_configurations_fn("sandbox-core")
set_output_dirs_fn("sandbox-core")
