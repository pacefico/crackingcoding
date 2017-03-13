#include <iostream>

using namespace std;

int fibonacci(int n) {
    if (n == 0 || n == 1){
      return n;
    }
    return fibonacci(n-1) + fibonacci(n-2);
}

void case0(){
  cout << fibonacci(6) << endl;
}
void case1(){

  for (size_t i = 0; i < 20; i++) {
    cout << "fibonnacci(" << i << ")=" << fibonacci(i) << endl;
  }
}

int main(){
  case1();
}

int main_from_test() {
    int n;
    cin >> n;
    cout << fibonacci(n);
    return 0;
}
