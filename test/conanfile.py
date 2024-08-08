from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps


class TesstRecipe(ConanFile):

    settings = ("os", "compiler", "build_type", "arch")
    generators = ("CMakeDeps", "CMakeToolchain")

    def requirements(self):
        self.requires("gtest/1.15.0")
    
    def layout(self):
        cmake_layout(self)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.bin = ["demo_unitTest"]
        


