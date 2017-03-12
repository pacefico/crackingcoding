#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <list>

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

struct Player {
    string name;
    int score;
};

bool compare(const Player& first, const Player& second){
  if (first.score > second.score){
    return true;
  }
  if (first.score == second.score){
    return first.name < second.name;
  }
  return false;
}

vector<Player> comparator(vector<Player> players) {
  sort(players.begin(), players.end(), compare);
  return players;
}

void buildCase(std::vector<string> v){
  std::vector<Player> players;
  for(uint i = 0; i < v.size(); i++){
    vector<string> values;
    values = splitString(v[i], ' ');
    Player p;
    p.name = values[0];
    p.score = atoi(values[1].c_str());
    players.push_back(p);
  }

  players = comparator(players);
  cout << endl;
  for (size_t i = 0; i < players.size(); i++) {
    cout << players[i].name << " " << players[i].score << endl;
  }
}

void case0(){
  std::vector<string> v;
  v = { "amy 100",
        "david 100",
        "heraldo 50",
        "aakansha 75",
        "aleksa 150" };
  buildCase(v);
}

void case1(){
  std::vector<string> v;
  v = { "amy 100",
        "david 100",
        "heraldo 50",
        "heraldo 52",
        "aakansha 75",
        "aleksa 150",
      "ale 150" };
  buildCase(v);
}

int main(){
  case1();
}

int main_from_test() {

    int n;
    cin >> n;
    vector< Player > players;
    string name;
    int score;
    for(int i = 0; i < n; i++){
        cin >> name >> score;
        Player p1;
        p1.name = name, p1.score = score;
        players.push_back(p1);
    }

    vector<Player > answer = comparator(players);
    for(int i = 0; i < answer.size(); i++) {
        cout << answer[i].name << " " << answer[i].score << endl;
    }
    return 0;
}
