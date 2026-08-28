// Engine.cpp ส่วนหลักของการคำนวน pso
#include "Engine.hpp"
#include "Fitness.hpp"
#include <random>
#include <cmath>

using namespace std;

EnginePSO::EnginePSO(int particlesB, int iterations, const vector<vector<double>> &data , const vector<int> &y_data ,int num_classes)
    : particles_(particlesB),
      iterations_(iterations),
      X(data),
      y(y_data),
      num_class(num_classes),
      n_features(data[0].size()),
      particles(particlesB, vector<int>(n_features)),
      velocity(particlesB, vector<double>(n_features)),
      pbest(particlesB, vector<int>(n_features)),
      pbest_score(particlesB),
      gbest(n_features),
      gbest_score(-std::numeric_limits<double>::infinity())
{}



  EnginePSO:: PSOResult EnginePSO::run_parallel(int n_threads)
{
    initialize();

    int block = particles_ / n_threads;
    int remainder = particles_ % n_threads;

    vector<thread> threads;

    for (int i = 0; i < n_threads; i++)
    {
        int start = i * block + min(i, remainder);
        int end = start + block;

        if (i < remainder)
            end++;

        threads.emplace_back(
            &EnginePSO::IterationLoop,
            this,
            start,
            end
        );
    }

    for (auto &t : threads)
        t.join();

    PSOResult result;
    result.best_features = gbest;
    result.best_score = gbest_score.load();

    return result;
}

void EnginePSO::IterationLoop(int start, int end)
{
    int patience = 20;
    int no_improve_count = 0;
    double local_best_known = gbest_score.load();

    for (int iter = 0; iter < iterations_; iter++)
    {
        vector<int> gbest_snapshot = gbest;
        
        update_velocity(start, end, gbest_snapshot);
        update_position(start, end);

        for (int i = start; i < end; i++)
        {

            double score ;
            if (num_class == 2) {
                score = evaluate_binary(particles[i], X, y); 
            } else {
                score = evaluate_multiclass(particles[i], X, y, num_class); 
            }

            if (score > pbest_score[i])
            {
                pbest_score[i] = score;
                pbest[i] = particles[i];
            }
            if (score > gbest_score.load())
            {
                lock_guard<mutex> lock(mtx); 
                
                if (score > gbest_score.load()) 
                {
                    gbest_score.store(score);
                    gbest = particles[i];
                }
            }
        }
        double current_global_best = gbest_score.load();

        if (current_global_best > local_best_known + 1e-9) 
        {
            local_best_known = current_global_best;
            no_improve_count = 0; 
        } 

        else no_improve_count++;   

        if (no_improve_count >= patience) break; 
        
    }
}

void EnginePSO::initialize()
{
    mt19937 gen(random_device{}());
    bernoulli_distribution binary(0.5);
    uniform_real_distribution<double> vel(-1, 1);

    gbest_score.store(-std::numeric_limits<double>::infinity());

    for (int i = 0; i < particles_; i++)
    {
        for (int j = 0; j < n_features; j++)
        {
            particles[i][j] = binary(gen);
            velocity[i][j] = vel(gen);
        }

        pbest[i] = particles[i];

        double score ;
        if (num_class == 2) {
            score = evaluate_binary(particles[i], X, y); 
        } else {
            score = evaluate_multiclass(particles[i], X, y, num_class); 
        }
        
        pbest_score[i] = score;

        if (score > gbest_score.load())
        {
            gbest_score.store(score);
            gbest = particles[i];
        }
    }
}

void EnginePSO::update_velocity(int start, int end, const vector<int> &gbest_snapshot)
{
    double w = 0.7;
    double c1 = 1.5;
    double c2 = 1.5;

    thread_local mt19937 gen(std::random_device{}() + std::hash<std::thread::id>{}(std::this_thread::get_id()));
    uniform_real_distribution<double> rand01(0, 1);

    for (int i = start; i < end; i++)
    {
        for (int j = 0; j < n_features; j++)
        {
            double r1 = rand01(gen);
            double r2 = rand01(gen);

            velocity[i][j] =
                w * velocity[i][j] + c1 * r1 * (pbest[i][j] - particles[i][j]) + c2 * r2 * (gbest_snapshot[j] - particles[i][j]);
        }
    }
}

void EnginePSO::update_position(int start, int end)
{
    thread_local mt19937 gen(std::random_device{}() + std::hash<std::thread::id>{}(std::this_thread::get_id()));
    uniform_real_distribution<double> rand01(0, 1);

    for (int i = start; i < end; i++)
    {
        for (int j = 0; j < n_features; j++)
        {
            double s = 1.0 / (1.0 + std::exp(-velocity[i][j]));

            particles[i][j] =
                (rand01(gen) < s) ? 1 : 0;
        }
    }
}