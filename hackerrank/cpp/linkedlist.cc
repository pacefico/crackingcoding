#include <iostream>
#include <string>
using namespace std;

struct Node{
  public:
    int data;
    struct Node* next;
};

Node * case0(){

  Node *nE;
  nE->data = 5;

  Node *nD;
  nD->data = 4;
  nD->next = nE;

  Node *nC;
  nC->data = 3;
  nC->next = nD;

  Node *nB;
  nB->data = 2;
  nB->next = nC;

  Node *nA;
  nA->data = 1;
  nA->next = nB;

  return nA;
}

bool has_cycle(Node* head){
  return 1;
}

const char* bool_cast(const bool b){
  return b ? "true" : "false";
}

int main(){

cout << "Linked List" << endl;

cout << bool_cast(1) << endl;

// cout << "case0(): has: " << bool_cast(has_cycle(case0())) << endl;

}
