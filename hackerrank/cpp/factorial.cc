#include <iostream>

using namespace std;

double factorial(double n) {
    if (n == 1 || n == 0){
      return 1;
    }
    return n * factorial(n-1);
}

void case0(){
  cout << factorial(6) << endl;
}

void case1(){
  for (size_t i = 0; i < 64; i++) {
    cout << "factorial(" << i << ")=" << factorial(i) << endl;
  }
}

int main(){
  case1();
}

int main_from_test() {
    int n;
    cin >> n;
    cout << factorial(n);
    return 0;
}
