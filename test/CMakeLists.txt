cmake_minimum_required(VERSION 3.15)

project(demo_unitTest)

# Include Conan-generated files
find_package(GTest REQUIRED)

set(test_src_files
${CMAKE_CURRENT_SOURCE_DIR}/src/test_main.cpp
)

add_executable(demo_unitTest 
${test_src_files}
)


target_link_libraries(demo_unitTest GTest::gtest GTest::gtest_main)

 
# Enable testing
enable_testing()
add_test(NAME demo_unitTest COMMAND your_tests)

