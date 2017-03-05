#include <map>
// #include <set>
// #include <list>
// #include <cmath>
// #include <ctime>
// #include <deque>
// #include <queue>
// #include <stack>
#include <string>
// #include <bitset>
// #include <cstdio>
// #include <limits>
#include <vector>
// #include <climits>
// #include <cstring>
// #include <cstdlib>
// #include <fstream>
// #include <numeric>
// #include <sstream>
// #include <iostream>
#include <algorithm>
// #include <unordered_map>
#include <iostream>
#include <cstdio>
#include <cassert>

using namespace std;

bool ransom_note(vector<string> magazine, vector<string> ransom) {
    map<string, int> my_magazine;

    for(vector<string>::iterator it = magazine.begin(); it != magazine.end(); ++it){
        pair< map<string,int>::iterator, bool> response;
        transform((*it).begin(), (*it).end(), (*it).begin(), ::tolower);
        response = my_magazine.insert( std::pair<string, int>(*it, 1));
        if (!response.second){
            map<string, int>::iterator value_it = my_magazine.find((*it));
            if (value_it != my_magazine.end()){
                value_it->second += 1;
            }
        }
    }
    int count = 0;
    for (vector<string>::iterator it = ransom.begin(); it != ransom.end(); ++it){
        map<string, int>::iterator word_it = my_magazine.find((*it));
        if (word_it != my_magazine.end()){
            if (word_it->second > 0){
                word_it->second -= 1;
                count +=1;
            }else {
                break;
            }
        } else {
            break;
        }
    }
    return count == ransom.size();
}

void case0(){
  //string magazine = "give me one grand today night me Me";
  //string ransom = "give one grand today";

  vector<string> magazine;
  magazine = {"give", "me", "one", "grand", "today", "night", "me"};
  vector<string> ransom;
  ransom = {"give", "one", "grand", "today"};

  bool response = ransom_note(magazine, ransom);
  assert(response == true);
}

int main(){
  case0();
}

int main_from_test(){
    int m;
    int n;
    cin >> m >> n;
    vector<string> magazine(m);
    for(int magazine_i = 0;magazine_i < m;magazine_i++){
       cin >> magazine[magazine_i];
    }
    vector<string> ransom(n);
    for(int ransom_i = 0;ransom_i < n;ransom_i++){
       cin >> ransom[ransom_i];
    }
    if(ransom_note(magazine, ransom))
        cout << "Yes\n";
    else
        cout << "No\n";
    return 0;
}
