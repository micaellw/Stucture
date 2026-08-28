// MainPSO.cpp รับข้อมูลจาก Main_CL.cpp แล้วส่งไปคำนวน
#include "MainPSO.hpp"
#include "Core/Engine.hpp"

using namespace std;
namespace py = pybind11;

ResultRun run_bpso(py::array_t<double> input_X , py::array_t<int> input_y ,int num_classes) {

    auto buf = input_X.unchecked<2>();
    auto buf_y = input_y.unchecked<1>();

    int rows = buf.shape(0);
    int cols = buf.shape(1);

    vector<vector<double>> X(
        rows, vector<double>(cols)
    );
    vector<int> y(rows);

    for (int i = 0; i < rows; i++){
        y[i] = buf_y(i);
        for (int j = 0; j < cols; j++){
            X[i][j] = buf(i, j);
        }
    }
    int amount_particles = 0;
    int iterations = 10 * cols;

    if (cols < 20)
        amount_particles = 15;
    else if (cols <= 50)
        amount_particles = 25;
    else if (cols <= 100)
        amount_particles = 40;
    else if (cols <= 300)
        amount_particles = 60;
    else if (cols <= 600)
        amount_particles = 80;
    else if (cols <= 1000)
        amount_particles = 100;
    else
        amount_particles = 125;  

    unsigned int cpuCount = thread::hardware_concurrency();

    if (cpuCount == 0) cpuCount = 2; 
    else cpuCount -= 2;

    EnginePSO engine(amount_particles, iterations, X , y ,num_classes);
    EnginePSO::PSOResult res;

    if (amount_particles < 20)
    {
        res = engine.run_parallel(1);
    }
    else
    {
        res = engine.run_parallel(cpuCount);
    }

    ResultRun result;

    result.best_features = res.best_features;
    result.best_score = res.best_score;

    return result;
}