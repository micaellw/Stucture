#Setup build for python send data to cpp
import os
from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..",".."))

def get_cpp_path(*paths):
    return os.path.join(BASE_DIR, "ML", "Computational_Intelligence", *paths)

cpp_sources = [
    get_cpp_path("Main_CI.cpp"),
    get_cpp_path("CI_Model", "PSO", "MainPSO.cpp"),
    get_cpp_path("CI_Model", "PSO", "Core", "Fitness.cpp"),
    get_cpp_path("CI_Model", "PSO", "Core", "Engine.cpp"),
]

ext_modules = [
    Pybind11Extension(
        "Main_CI",
        cpp_sources,
        include_dirs=[get_cpp_path("")], 
        cxx_std=17,
    ),
]

setup(
    name="Main_CI",
    version="0.1",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    install_requires=[
        "numpy",
    ],
)