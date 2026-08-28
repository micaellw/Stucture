// Main_Cl รอรับข้อมูลจาก python
#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <pybind11/stl.h>
#include "CI_Model/PSO/MainPSO.hpp"
namespace py = pybind11;


py::tuple run(py::array_t<double> input_X , py::array_t<int> input_y ,int num_classes) {
    ResultRun result = run_bpso(input_X, input_y, num_classes);

    return py::make_tuple(
        result.best_features,
        result.best_score
    );
}

PYBIND11_MODULE(Main_CI, m) {
    m.def("run", &run, "A function");
}