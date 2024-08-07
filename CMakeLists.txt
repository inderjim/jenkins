cmake_minimum_required(VERSION 3.1)

project(hello_world)

add_executable(hello_world src/main.c)

install(TARGETS hello_world)

install(FILES src/main.c DESTINATION src)
