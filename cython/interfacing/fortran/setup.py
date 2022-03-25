"""
Example setup.py file for compiling and linking cython to a fortran module.
Compile with 'python setup.py build_ext --inplace'
"""
from setuptools import setup, find_packages, Extension
from Cython.Distutils import build_ext
from numpy import get_include  # only needed if numpy is used in .pyx file

from subprocess import run  # For compiling fortran files

fortran_compiler = "gfortran"
compiler_flags = ["-O3", "-fPIC"]
# -c compiles modules without linking
fortran_module_compilation = [
    fortran_compiler,
    "fortmod.f90",
    "-c",
    "-o",
    "fortmod.o",
] + compiler_flags
shared_object_compilation = [
    fortran_compiler,
    "fort_interface.f90",
    "-c",
    "-o",
    "fort_interface.o",
] + compiler_flags

# Compiling fortran modules
print(" ".join(fortran_module_compilation))
run(fortran_module_compilation)
print(" ".join(shared_object_compilation))
run(shared_object_compilation)

# Removing existing build to force recompilation
run(["rm", "-r", "build/", "fortmod.cpython-39-x86_64-linux-gnu.so"])

ext_modules = [
    Extension(  # module name to create (.so file)
        "fortmod",
        # cython source file
        ["fort_interface.pyx"],
        # other compile args for fortran compiler
        extra_compile_args=["-fPIC", "-O3"],
        # fortran modules to link
        extra_link_args=["fortmod.o", "fort_interface.o"],
    )
]


setup(
    name="fortran_interface",
    cmdclass={"build_ext": build_ext},
    # Needed if building with NumPy. (not used here, but left for reference.
    # This includes the NumPy headers when compiling.
    include_dirs=[get_include()],
    ext_modules=ext_modules,
)
