#include <iostream>
#include <algorithm>

/*
Problem Description
Task. The goal in this problem is to find the minimum number of coins needed to change the input value
(an integer) into coins with denominations 1, 5, and 10.
Input Format. The input consists of a single integer m.
*/

int get_change(int m) {
  int coins[] = {10, 5, 1};
  int n = 0;
  int i = 0;

  while (1) {
    if (m == 0){
      return n;
    }
    int coin = coins[i];
    while (coin <= m){
      n += 1;
      m -= coin;
    }
    i += 1;
  }
  return n;
}

int main() {
  int m;
  std::cin >> m;
  std::cout << get_change(m) << '\n';
}
