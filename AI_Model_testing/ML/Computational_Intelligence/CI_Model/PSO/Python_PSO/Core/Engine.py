# Engine.py - Python equivalent of Engine.cpp
# Main calculation engine for Binary Particle Swarm Optimization (BPSO)

import math
import random
from .Fitness import evaluate_binary, evaluate_multiclass


class EnginePSO:
    """
    Exact 1:1 translation of C++ EnginePSO in Engine.cpp
    """
    def __init__(self, particles_count, iterations, data, y_data, num_classes):
        self.particles_ = particles_count
        self.iterations_ = iterations
        self.X = data
        self.y = y_data
        self.num_class = num_classes
        self.n_features = len(data[0])

        self.particles = [[0] * self.n_features for _ in range(self.particles_)]
        self.velocity = [[0.0] * self.n_features for _ in range(self.particles_)]

        self.pbest = [[0] * self.n_features for _ in range(self.particles_)]
        self.pbest_score = [-float('inf')] * self.particles_

        self.gbest = [0] * self.n_features
        self.gbest_score = -float('inf')

    def initialize(self):
        """
        Initialize particles with Bernoulli(0.5) and velocity with Uniform(-1, 1)
        """
        self.gbest_score = -float('inf')

        for i in range(self.particles_):
            for j in range(self.n_features):
                self.particles[i][j] = 1 if random.random() < 0.5 else 0
                self.velocity[i][j] = random.uniform(-1.0, 1.0)

            self.pbest[i] = list(self.particles[i])

            if self.num_class == 2:
                score = evaluate_binary(self.particles[i], self.X, self.y)
            else:
                score = evaluate_multiclass(self.particles[i], self.X, self.y, self.num_class)

            self.pbest_score[i] = score

            if score > self.gbest_score:
                self.gbest_score = score
                self.gbest = list(self.particles[i])

    def update_velocity(self, gbest_snapshot):
        """
        Update particle velocities using standard PSO formula:
        v = w*v + c1*r1*(pbest - x) + c2*r2*(gbest - x)
        """
        w = 0.7
        c1 = 1.5
        c2 = 1.5

        for i in range(self.particles_):
            for j in range(self.n_features):
                r1 = random.random()
                r2 = random.random()
                self.velocity[i][j] = (
                    w * self.velocity[i][j]
                    + c1 * r1 * (self.pbest[i][j] - self.particles[i][j])
                    + c2 * r2 * (gbest_snapshot[j] - self.particles[i][j])
                )

    def update_position(self):
        """
        Update particle binary positions using Sigmoid transfer function:
        s(v) = 1 / (1 + exp(-v))
        x = 1 if rand() < s(v) else 0
        """
        for i in range(self.particles_):
            for j in range(self.n_features):
                s = 1.0 / (1.0 + math.exp(-self.velocity[i][j]))
                self.particles[i][j] = 1 if random.random() < s else 0

    def run(self):
        """
        Main optimization loop with early stopping patience of 20 iterations
        """
        self.initialize()

        patience = 20
        no_improve_count = 0
        local_best_known = self.gbest_score

        for _ in range(self.iterations_):
            gbest_snapshot = list(self.gbest)

            self.update_velocity(gbest_snapshot)
            self.update_position()

            for i in range(self.particles_):
                if self.num_class == 2:
                    score = evaluate_binary(self.particles[i], self.X, self.y)
                else:
                    score = evaluate_multiclass(self.particles[i], self.X, self.y, self.num_class)

                if score > self.pbest_score[i]:
                    self.pbest_score[i] = score
                    self.pbest[i] = list(self.particles[i])

                if score > self.gbest_score:
                    self.gbest_score = score
                    self.gbest = list(self.particles[i])

            current_global_best = self.gbest_score

            if current_global_best > local_best_known + 1e-9:
                local_best_known = current_global_best
                no_improve_count = 0
            else:
                no_improve_count += 1

            if no_improve_count >= patience:
                break

        return self.gbest, self.gbest_score
