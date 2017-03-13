#include <cstdio>
#include <vector>
#include <iostream>

using namespace std;

/*
 * Arista Network (Dublin) test: 3/13/2017
 *  Complete the function below.
 */

string FormatString(string S) {
  string stringClean;
  for (size_t i = 0; i < S.size(); i++) {
    if (S[i] != ' ' && S[i] != '-'){
      stringClean += S[i];
    }
  }
  string newString;
  int count = 0;
  int left = stringClean.size();
  for (size_t i = 0; i < stringClean.size(); i++) {
    newString += stringClean[i];
    count ++;
    left --;
    if (count == 2 && left == 2){
      newString += " ";
      count = 0;
    }
    if(count == 3 && left > 0){
      newString += " ";
      count = 0;
    }
  }
  return newString;
}

string FormatStringOLD(string S) {

  if (S.size() <= 3){
    return S;
  }
  int count = 0;
  int left = S.size();
  string newString;

  for(string::iterator it = S.begin(); it != S.end(); ++it){

    if (count == 3 && left >= 2){
      newString += " ";
      count = 0;
    }
    if (count == 2 && left == 2){
      newString += " ";
      count = 0;
    }
    if (*it != ' ' && *it != '-'){
      newString += *it;
      count ++;
    }
    left --;
    //cout << newString << " C: " << count << endl;
  }
  return newString;
}

void testcase(string s1){
    cout << "old: " << s1 << "    new: " << FormatString(s1) << "[end]" << endl;
}

void case0(){
  string s1 = "00-44 48 5555 8361";
  testcase(s1);
}
void case1(){
  string s1 = "0 - 22 1985--324";
  testcase(s1);
}
void case2(){
  string s1 = "ABC372654";
  testcase(s1);
}
void case3(){
  string s1 = "23";
  testcase(s1);
}
void case4(){
  string s1 = "2 3 55--89 AAA";
  testcase(s1);
}
void case5(){
  string s1 = "2 3 55";
  testcase(s1);
}
void case6(){
  string s1 = "2-3 5";
  testcase(s1);
}

int main(){
  case0();
  case1();
  case2();
  case3();
  case4();
  case5();
  case6();

}
