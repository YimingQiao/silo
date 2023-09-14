# Set the project name
project(db_compress)

# cmake version
cmake_minimum_required(VERSION 3.18)

# Use C++ 17
set(CMAKE_CXX_STANDARD 17)

if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Release CACHE STRING "Build type" FORCE)
endif()

set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} -march=native")

# Glob all source files, named SRC_FILES
file(GLOB_RECURSE SRC_FILES src/*.cpp)

# Create a sources variable with a link to all cpp files to compile
add_library(${PROJECT_NAME} STATIC ${SRC_FILES})

target_include_directories(${PROJECT_NAME}
        PUBLIC
        ${PROJECT_SOURCE_DIR}/include
)