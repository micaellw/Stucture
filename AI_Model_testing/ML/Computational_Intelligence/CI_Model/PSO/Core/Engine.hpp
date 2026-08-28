// Inteface ของ Engine 
#ifndef ENGINE_HPP
#define ENGINE_HPP
#include <vector>
#include <mutex>
#include <thread>
#include <atomic>

using namespace std;

class EnginePSO{

public:

EnginePSO(int particlesB, int iterations, const vector<vector<double>>& data, const std::vector<int> &y_data ,int num_classes);

struct PSOResult
{
    vector<int> best_features;
    double best_score;
};

PSOResult run_parallel(int n_threads);

private:

    int particles_;
    int iterations_;
    int n_features ;
    int num_class;

    vector<vector<double>> X;
    vector<int> y;

    vector<vector<int>> particles;
    vector<vector<double>> velocity;

    vector<vector<int>> pbest;
    vector<double> pbest_score;

    vector<int> gbest;
    atomic<double> gbest_score;

    mutex mtx;   
    void IterationLoop(int start, int end);
    void initialize();
    void update_velocity(int start, int end , const vector<int>& gbest_snapshot);
    void update_position(int start, int end);

};

#endif