

set(src_files
${CMAKE_CURRENT_SOURCE_DIR}/src/main.c
)

add_executable(demo 
${src_files}
)

install(TARGETS demo)

install(FILES ${src_files} DESTINATION src)
