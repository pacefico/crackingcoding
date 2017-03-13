#include <fstream>
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
    this->count = 0;
    this->letter = letter;
    this->complete = false;
  }

  void add(string item){
    string::iterator it = item.begin();
    TrieNode *current;
    current = this;
    while(it != item.end()){
        TrieNode *exist;
        exist = this->getExist(*it, current);

        if (exist == NULL){
          exist = new TrieNode(*it);
          exist->complete = it + 1 == item.end();
          exist->count ++;
          current->next.insert(pair<char, TrieNode>(*it, *exist));
        } else {
          exist->count ++;
          exist->complete = it + 1 == item.end() || exist->complete;
        }
        current = &current->next[*it];
        exist = NULL;
        ++it;
    }
  }

  TrieNode* getExist(char letter, TrieNode *current){
    map<char, TrieNode>::iterator it;
    it = current->next.find(letter);
    if (it != current->next.end()){
      return &current->next[letter];
    }
    return NULL;
  }

  int find(string item){
    TrieNode * current;
    current = this;
    int count = 0;
    string::iterator it = item.begin();
    while(it != item.end()){
      TrieNode * exist;
      exist = getExist(*it, current);
      if (exist != NULL){
        current = &current->next[*it];
        if (current != NULL && it +1 == item.end() && current->letter == *it){
          count = current->count;
          break;
        }
      } else {
        break;
      }
      exist = NULL;
      ++it;
    }
    return count;
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
    int response = this->root->find(item);
    return response;
  }
};

void case0(){
  std::vector<string> v;
  v = {   "add hack",
            "add hac",
            "add ha",
            "find hac",
            "add hackerrank",
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
        printf("%d\n", tries->find(values[1].c_str()));
      }
    }
}

void case1(){
  Tries *tries;
  tries = new Tries();
  string line;
  string line_output;
  ifstream input_file ("..//artifacts/tries/test2/input.txt");
  ifstream output_file ("..//artifacts/tries/test2/output.txt");
  int count = 0;
  if (input_file.is_open() && output_file.is_open())
  {
    while ( getline (input_file,line) )
    {
      std::vector<string> values;
      values = splitString(line, ' ');
      if (values[0] == "add"){
        tries->add(values[1].c_str());
      } else if (values[0] == "find"){
        int result = tries->find(values[1].c_str());
        getline (output_file,line_output);
        if (result != atoi(line_output.c_str())){
          std::cout << "false: " << count << " expect: " << line_output << '\n';
        }

      }
      count ++;
    }
    input_file.close();
  }
}

int main(){
  case1();
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
