from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps


class demoRecipe(ConanFile):
    name = "demo"
    version = "1.0"

    # Binary configuration
    settings = ("os", "compiler", "build_type", "arch")
    generators = ("CMakeDeps", "CMakeToolchain")
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt","common/CMakeLists.txt", "common/src/*"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    #def requirements(self):
    #    self.requires("gtest/1.15.0")
    
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
        self.cpp_info.bin = ["demo"]
        
    def test(self):
        if can_run(self):
            cmd = os.path.join(self.cpp.build, "demo")
            self.run(cmd, env="conanrun")

        


