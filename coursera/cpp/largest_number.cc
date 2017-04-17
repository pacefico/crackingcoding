#include <iostream>
#include <vector>
// #include <iomanip>
#include <algorithm>
#include <string>

using namespace std;

bool comparator(int i, int j){
  string istr = to_string(i);
  string jstr = to_string(j);

  if(istr.size() != jstr.size()){
    string ij = istr + jstr;
    string ji = jstr + istr;
    return stoi(ij) >= stoi(ji);
  } else {
    return i >= j;
  }
}

string largest_number(vector<int> a){
  sort(a.begin(), a.end(), comparator);

  string res = "";
  for (size_t i = 0; i < a.size(); i++) {
    res += to_string(a[i]);
  }
  return res;
}

void test0(){
  std::vector<int> v;
  v = {21, 2};
  std::cout << "r: " << largest_number(v) << std::endl;
}

void test1(){
  std::vector<int> v;
  v = {9, 4, 6, 1, 9};
  std::cout << "r: " << largest_number(v) << std::endl;
}

void test2(){
  std::vector<int> v;
  v = {23, 39, 92};
  std::cout << "r: " << largest_number(v) << std::endl;
}

int main1(){
  // test0();
  // test1();
  test2();
  return 0;
}

int main(){
  int n;
  std::cin >> n;
  vector<int> values(n);
  for (int i = 0; i < n; i++) {
    std::cin >> values[i];
  }
 std::cout << largest_number(values) << std::endl;
  return 0;
}
