// #include <map>
// #include <set>
// #include <list>
// #include <cmath>
// #include <ctime>
// #include <deque>
// #include <queue>
// #include <stack>
// #include <string>
// #include <bitset>
// #include <cstdio>
// #include <limits>
// #include <vector>
// #include <climits>
// #include <cstring>
// #include <cstdlib>
// #include <fstream>
// #include <numeric>
// #include <sstream>
// #include <iostream>
// #include <algorithm>
// #include <unordered_map>

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <stack>
#include <queue>
#include <sstream>
#include <cstdlib>
#include <string>
#include <map>
using namespace std;

vector<string> splitString(string command, char delim){
  stringstream ss(command);
  string item;
  vector<string> elements;
  while(getline(ss, item, delim)){
    elements.push_back(item);
  }
  return elements;
}

class TrieNode{
public:
  bool complete;
  int count;
  char letter;
  map<char, TrieNode> next;

  TrieNode(char letter){
    this->count = 0;
    this->letter = letter;
    this->complete = false;
  }

  void add(string item){
    std::cout << "adding:" << item << '\n';

    string::iterator it = item.begin();
    TrieNode *current;
    current = this;
    while(it != item.end() and current != NULL){
        TrieNode *exist;
        exist = NULL;
        this->getExist(*it, exist);

        if (exist == NULL){
          std::cout << "not exist: " << *it << '\n';
        }

        ++it;
    }

  }

  void getExist(char letter, TrieNode *node){
    map<char, TrieNode>::iterator it;
    it = this->next.find(letter);
    if (it != this->next.end()){
      node = &it->second;
      std::cout << "exist: " << letter << '\n';
    }
  }

};

class Tries{

public:
  TrieNode *root;

  Tries(){
    this->root = new TrieNode('*');
  }

  void add(string item){
    this->root->add(item);
  }

};

void case0(){
  std::vector<string> v;
  v = {"add hack",
            "add hac",
            "add ha"
            // "find hac",
            // "add hackerrank",
            // "add hackk",
            // "add hackee",
            // "find ac",
            // "add ack",
            // "add acki",
            // "add acka",
            // "add ac",
            // "add hackker",
            // "add rank",
            // "find hac",
            // "find ha",
            // "find hak",
            // "find h",
            // "find ac"
          };
    Tries *tries;
    tries = new Tries();

    for (size_t i = 0; i < v.size(); ++i) {
      std::vector<string> values;
      values = splitString(v[i], ' ');
      if (values[0] == "add"){
        tries->add(values[1].c_str());
      }
    }

}

int main(){
  case0();
}

int main_from_test(){
    int n;
    cin >> n;
    for(int a0 = 0; a0 < n; a0++){
        string op;
        string contact;
        cin >> op >> contact;
    }
    return 0;
}
