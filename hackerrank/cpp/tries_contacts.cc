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

  TrieNode(){}

  TrieNode(char letter){
    this->count = 1;
    this->letter = letter;
    this->complete = false;
  }

  void add(string item){
    std::cout << "\nadding: " << item << " on: " << this->letter << '\n';

    string::iterator it = item.begin();
    TrieNode *current;
    current = this;
    while(it != item.end()){
        //std::cout << "it: " << *it << '\n';
        TrieNode *exist;
        exist = this->getExist(*it, current);

        if (exist == NULL){
          //std::cout << "not exist: " << *it << '\n';
          exist = new TrieNode(*it);
          exist->complete = it + 1 == item.end();
          current->next.insert(pair<char, TrieNode>(*it, *exist));
          std::cout << "adding: " << *it << " on: " << current->letter << " next size: " << current->next.size() << '\n';
        } else {
          exist->count += 1;
          exist->complete = it + 1 == item.end() || exist->complete;
          std::cout << "exist: " << exist->letter << " c:" << exist->count << " end: " << exist->complete << '\n';
        }

        current = &current->next[*it];
        ++it;
    }
    //current = this;

  }

  TrieNode* getExist(char letter, TrieNode *current){
    //std::cout << "finding: " << letter << " on: " << current->letter << " size: " << current->next.size() << '\n';
    map<char, TrieNode>::iterator it;
    it = current->next.find(letter);
    if (it != current->next.end()){
      return &current->next[letter];
    }
    return NULL;
  }

  int find(string item){
    std::cout << "\nfinding: " << item << '\n';
    //map<char, TrieNode>::iterator it;
    TrieNode * current;
    current = this;
    string::iterator it = item.begin();
    while(it != item.end()){
      TrieNode * exist;
      exist = getExist(*it, current);
      if (exist != NULL){
        current = &current->next[*it];
        if (current != NULL && it +1 == item.end()){
          printf("%c\n",  current->letter);
          return current->count;
        }
      }
      ++it;
    }


    return 0;
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
  int find(string item){
    return this->root->find(item);
  }

};

void case0(){
  std::vector<string> v;
  v = {   //"add hack",
            "add hac",
            "add ha",
            "add hackerrank",
            "find hac",
            "add hackk",
            "add hackee",
            "find ac",
            "add ack",
            "add acki",
            "add acka",
            "add ac",
            "add hackker",
            "add rank",
            "find hac",
            "find ha",
            "find hak",
            "find h",
            "find ac"
          };
    Tries *tries;
    tries = new Tries();

    for (size_t i = 0; i < v.size(); ++i) {
      std::vector<string> values;
      values = splitString(v[i], ' ');
      if (values[0] == "add"){
        tries->add(values[1].c_str());
      } else if (values[0] == "find"){
        printf("%d", tries->find(values[1].c_str()));
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
