#include <vector>
#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

vector<int> array_left_rotation(vector<int> a, int n, int k) {
    for (size_t i = 0; i < k; i++) {
      vector<int>::iterator val = a.begin();
      a.push_back(*val);
      a.erase(a.begin());
    }
    for (size_t i = 0; i <= k; i++) {
      printf("%d ", a[i]);
    }
    return a;
}

void case0(){
  int values[] = {1,2,3,4,5};
  int n = 5;
  int k = 4;
  vector<int> v(values, values+sizeof(values)/sizeof(int));

  int expected[] = { 5,1,2,3,4 };
  std::vector<int> new_v = array_left_rotation(v, n, k);
  for (size_t i = 0; i <= n; i++) {
    vector<int>::iterator val = new_v.begin() +i;
    if (*val != expected[i]){
      printf("assertion error!\n");
      return;
    }
  }
  printf("assertion OK!\n");
}

int main(){
  case0();
}

int main_from_test(){
    int n;
    int k;
    cin >> n >> k;
    vector<int> a(n);
    for(int a_i = 0;a_i < n;a_i++){
        cin >> a[a_i];
    }
    vector<int> output = array_left_rotation(a, n, k);
    for(int i = 0; i < n;i++)
        cout << output[i] << " ";
    cout << endl;
    return 0;
}
