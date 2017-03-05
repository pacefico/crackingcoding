#include <string>
#include <iostream>
#include <cstdio>
#include <map>
#include <algorithm>
#include <cassert>

using namespace std;

int countString(string complete, const char tofind){
  int count = 0;
  size_t nPos = complete.find(tofind, 0);
  while(nPos != string::npos){
    count ++;
    nPos = complete.find(tofind,nPos+1);
  }
  return count;
}

map<char,char> toMap(string complete){
  std::map<char,char> mymap;
  for (string::iterator it = complete.begin(); it != complete.end(); ++it) {
    mymap.insert ( std::pair<char,char>(*it,*it) );
  }
  return mymap;
}

int number_needed(string a, string b) {
  map<char, char> result = toMap(a);
  int count = 0;
  for (map<char,char>::iterator it = result.begin(); it != result.end(); ++it) {
    count += min(int(countString(a, it->first)), int(countString(b, it->first)));
  }
  return (a.length() + b.length()) - 2*count;
}

void case0(){
  string a = "abc";
  string b = "cde";

  int n = number_needed(a, b);
  printf("\nresult: %d\n", n);
  assert(n == 4);
}

void case1(){
  string a = "gwoydkkstkgaluglmwusqlpgozlvocxskfrrfhlowwzybguzps";
  string b = "qlkwlpwhbtuefedscyeualrzfdnzks";

  int n = number_needed(a, b);
  printf("\nresult: %d\n", n);
  assert(n == 30);
}

void case2(){
  string a="afaaa";
  string b="afff";

  int n = number_needed(a, b);
  printf("\nresult: %d\n", n);
  assert(n == 5);
}

void case3(){
  string a="bacdc";
  string b="dcbad";

  int n = number_needed(a, b);
  printf("\nresult: %d\n", n);
  assert(n == 2);
}

int main(){
  case0();
  case1();
  case2();
  case3();
}

int main_from_test(){
    string a;
    cin >> a;
    string b;
    cin >> b;
    cout << number_needed(a, b) << endl;
    return 0;
}
