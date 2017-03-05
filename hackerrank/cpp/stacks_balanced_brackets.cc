// #include <map>
// #include <set>
// #include <list>
// #include <cmath>
// #include <ctime>
// #include <deque>
// #include <queue>
#include <stack>
// #include <string>
// #include <bitset>
// #include <cstdio>
// #include <limits>
// #include <vector>
// #include <climits>
// #include <cstring>
#include <cstdlib>
// #include <fstream>
// #include <numeric>
// #include <sstream>
#include <iostream>
#include <algorithm>
// #include <unordered_map>
#include <cassert>

using namespace std;

int contains_on(vector<string> vec, char bracket){
  for(size_t i = 0; i < vec.size(); ++i){
    if (vec[i][0] == bracket){
      return i;
    }
  }
  return -1;
}

bool is_balanced(string expression) {
  stack<char> my_stack;
  vector<string> start;
  start = {"{", "[", "("};
  vector<string> end;
  end = {"}", "]", ")"};

  for(string::iterator it = expression.begin(); it != expression.end(); ++it){
    int ret = contains_on(start, (*it));
    if (ret > -1){
      my_stack.push((*it));
    } else {
      if(my_stack.size() > 0){
        char element = my_stack.top();
        int idx = contains_on(end, (*it));
        if (!(idx > -1 && element == start[idx][0])){
          return false;
        } else {
          my_stack.pop();
        }
      } else {
        return false;
      }
    }
  }
  if (my_stack.size() > 0){
    return false;
  }
  return true;
}

void case0(){
  string brackets = "{[()]}";
  bool response = is_balanced(brackets);
  assert(response == true);
}

void case1(){
  string brackets = "{[(])}";
  bool response = is_balanced(brackets);
  assert(response == false);
}

void case2(){
  string brackets = "{{[[(())]]}}[";
  bool response = is_balanced(brackets);
  assert(response == false);
}

void case3(){
  string brackets = "{{[[(())]]}}[({})]";
  bool response = is_balanced(brackets);
  assert(response == true);
}

int main(){
  case0();
  case1();
  case2();
  case3();
}

int main_from_test(){
    int t;
    cin >> t;
    for(int a0 = 0; a0 < t; a0++){
        string expression;
        cin >> expression;
        bool answer = is_balanced(expression);
        if(answer)
            cout << "YES\n";
        else cout << "NO\n";
    }
    return 0;
}
