#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;

void swap(int *a, int *b){
  int *temp;
  temp = a;
  b = a;
  a = temp;
}

void sort(vector<int> a){
  int totalSwaps = 0;
  uint n = a.size();
  for (int i = 0; i < n; i++) {
    // Track number of elements swapped during a single array traversal
    int numberOfSwaps = 0;
    for (int j = 0; j < n - 1; j++) {
        // Swap adjacent elements if they are in decreasing order
        if (a[j] > a[j + 1]) {
            swap(a[j], a[j + 1]);
            numberOfSwaps++;
        }
    }
    // If no elements were swapped during a traversal, array is sorted
    if (numberOfSwaps == 0) {
        break;
    }
    totalSwaps += numberOfSwaps;
  }
  cout << "Array is sorted in " << totalSwaps << " swaps." << endl;
  cout << "First Element: " << a[0] << endl;
  cout << "Last Element: " << a[n-1] << endl;
}

void case0(){
  sort({3,2,1});
}

void case1(){
  vector<int> v;
  int n0 = 1;
  int n = 600;
  int max = 6000000;

  for (uint i = 0; i < n; i++){
    int number = rand() % max + n0;
    v.push_back(number);
  }
  sort(v);
}

void case2(){
  sort({1, 2, 3});
}

void case3(){
  vector<int> v;
  int n = 600;
  int max = 6000000;

  for (uint i = 0; i < n; i++){
    int number = i + 1;
    v.push_back(number);
  }
  sort(v);
}

void case4(){
  sort({1, 2});
}

void case5(){
  sort({2, 1});
}

int main(){
  cout << endl;
  cout << "case 0" << endl;
  case0();

  cout << endl;
  cout<< "case 1" << endl;
  case1();

  cout << endl;
  cout << "case 2" << endl;
  case2();

  cout << endl;
  cout << "case 3" << endl;
  case3();

  cout << endl;
  cout << "case 4" << endl;
  case4();

  cout << endl;
  cout << "case 5" << endl;
  case5();
}

int main_from_test(){
    int n;
    cin >> n;
    vector<int> a(n);
    for(int a_i = 0;a_i < n;a_i++){
       cin >> a[a_i];
    }
    return 0;
}
