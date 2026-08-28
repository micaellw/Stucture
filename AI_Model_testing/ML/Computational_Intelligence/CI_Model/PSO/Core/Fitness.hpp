//Inteface ของ Fitness 
#ifndef FITNESS_HPP
#define FITNESS_HPP

#include <vector>

double evaluate_binary(
    const std::vector<int>& mask,
    const std::vector<std::vector<double>>& X,
    const std::vector<int>& y
);
double evaluate_multiclass(
    const std::vector<int>& mask, 
    const std::vector<std::vector<double>>& X, 
    const std::vector<int>& y, 
    int num_classes);

#endif