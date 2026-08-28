// Inteface ของ MainPSO 
#ifndef MAINPSO_HPP
#define MAINPSO_HPP

#include <vector>
#include <pybind11/numpy.h>
namespace py = pybind11;

struct ResultRun
{
    std::vector<int> best_features;
    double best_score;
};
ResultRun run_bpso(py::array_t<double> input , py::array_t<int> input_y ,int num_classes);

#endif