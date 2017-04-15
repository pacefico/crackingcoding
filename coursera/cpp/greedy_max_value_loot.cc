/*
Problem Introduction
A thief finds much more loot than his bag can fit. Help him to find the most valuable combination
of items assuming that any fraction of a loot item can be put into his bag.

Problem Description
Task. The goal of this code problem is to implement an algorithm for the fractional knapsack problem.
Input Format. The first line of the input contains the number n of items and the capacity W of a knapsack.
The next n lines define the values and weights of the items. The i-th line contains integers vi and wi—the
value and the weight of i-th item, respectively.

Constraints.
    1 ≤ n ≤ 10^3
    0 ≤ W ≤ 2 · 10^6
    0 ≤ vi ≤ 2 · 10^6
    0 < wi ≤ 2 · 10^6
    for all 1 ≤ i ≤ n.
*/

#include <iostream>
#include <vector>
#include <iomanip>
#include <algorithm>

using std::vector;

struct Values {
  int weight;
  int value;
};

bool compare(const Values& first, const Values& second){
  double val1 = (double) first.value / first.weight;
  double val2 = (double) second.value / second.weight;
  return val1 > val2;
}

vector<Values> comparator(vector<Values> values) {
  sort(values.begin(), values.end(), compare);
  return values;
}

vector<Values> get_sorted(vector<int> weights, vector<int> values){
  vector<Values> new_values;
  for (size_t i = 0; i < weights.size(); i++) {
    Values val;
    val.weight = weights[i];
    val.value = values[i];
    new_values.push_back(val);
  }
  return comparator(new_values);
}

double get_optimal_value(int capacity, vector<int> weights, vector<int> values) {
  double value = 0.0;
  int currentWeight = 0;
  // sort the input to get max value/weight from items
  vector<Values> sortedValues = get_sorted(weights, values);

  for (size_t i = 0; i < sortedValues.size(); i++) {
    if(currentWeight == capacity){
      return value;
    }
    if (currentWeight + sortedValues[i].weight <= capacity){
      // adding item one-by-one from sorted list
      value += sortedValues[i].value;
      currentWeight += sortedValues[i].weight;
    } else {
      // adding fraction of capacity
      int remain = capacity - currentWeight;
      value += (double) sortedValues[i].value * ((double) remain / sortedValues[i].weight);
      currentWeight += remain;
    }
  }
  return value;
}

void run(int capacity, vector<int> weights, vector<int> values){
  double optimal_value = get_optimal_value(capacity, weights, values);
  std::cout.precision(10);
  std::cout << optimal_value << std::endl;
}

void test0(){
  int n = 3;
  int capacity = 50;
  vector<int> values(n);
  values = {60, 100, 120};
  vector<int> weights(n);
  weights = {20, 50, 30};
  run(capacity, weights, values);
}

void test1(){
  int n = 1;
  int capacity = 10;
  vector<int> values(n);
  values = {500};
  vector<int> weights(n);
  weights = {30};
  run(capacity, weights, values);
}

void test2(){
  int n = 4;
  int capacity = 60;
  vector<int> values(n);
  values = {60, 100, 120, 120};
  vector<int> weights(n);
  weights = {20, 50, 30, 40};
  run(capacity, weights, values);
}

int main1(){
  test0();
  test1();
  test2();
  return 0;
}

int main() {
  int n;
  int capacity;
  std::cin >> n >> capacity;
  vector<int> values(n);
  vector<int> weights(n);
  for (int i = 0; i < n; i++) {
    std::cin >> values[i] >> weights[i];
  }

  double optimal_value = get_optimal_value(capacity, weights, values);

  std::cout << std::setprecision(10);
  std::cout << optimal_value << std::endl;
  return 0;
}
