#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <stack>
#include <queue>
#include <sstream>
#include <cstdlib>
using namespace std;

vector<int> splitInt(string s, char delim){
  stringstream ss(s);
  string item;
  vector<int> elements;
  while(getline(ss, item, delim)){
    elements.push_back(stoi(item));
  }
  return elements;
}

vector<string> splitString(string s, char delim){
  stringstream ss(s);
  string item;
  vector<string> elements;
  while(getline(ss, item, delim)){
    elements.push_back(item);
  }
  return elements;
}


class MyQueue {

    public:
        stack<int> stack_newest_on_top, stack_oldest_on_top;
        void push(int x) {
          stack_newest_on_top.push(x);
        }

        void swap(){
          if (stack_oldest_on_top.size() == 0){
            //printf("size==0\n");
              while (stack_newest_on_top.size() > 0){
                stack_oldest_on_top.push(stack_newest_on_top.top());
                stack_newest_on_top.pop();
              }
          }
        }

        void pop() {
          swap();
          if (stack_oldest_on_top.size() > 0){
            stack_oldest_on_top.pop();
          }
        }

        int front() {
          swap();
          int response = 0;
          if (stack_oldest_on_top.size() > 0){
            response = stack_oldest_on_top.top();
          }
          return response;
        }
};

void case0(){
  string test = "1 42:2:1 14:3:1 28:3:1 60:1 78:2:2:3";

  MyQueue q;
  std::vector<string> v = splitString(test, ':');
  for (size_t i = 0; i < v.size(); i++) {
    string s = v[i].c_str();
    printf("cmd=%s\n", v[i].c_str());
    if (s[0] == '1'){
      vector<int> values = splitInt(s, ' ');
      q.push(values[1]);
      //printf("%s int=%d\n", v[i].c_str(),values[1] );
    } else if(s[0] == '2'){
      q.pop();
    } else {
      cout << q.front() << endl;
    }
  }


}

int main(){
  case0();
}

int main_from_test() {
    MyQueue q1;
    int q, type, x;
    cin >> q;

    for(int i = 0; i < q; i++) {
        cin >> type;
        if(type == 1) {
            cin >> x;
            q1.push(x);
        }
        else if(type == 2) {
            q1.pop();
        }
        else cout << q1.front() << endl;
    }
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    return 0;
}
