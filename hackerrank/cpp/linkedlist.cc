#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

struct Node{
  public:
    int data;
    struct Node* next;
};

void case0(Node &node){

  Node *nE = new Node();
  nE->data = 5;
  nE->next = NULL;

  Node *nD = new Node();
  nD->data = 4;
  nD->next = nE;

  Node *nC = new Node();
  nC->data = 3;
  nC->next = nD;

  Node *nB = new Node();
  nB->data = 2;
  nB->next = nC;

  Node *nA = new Node();
  nA->data = 1;
  nA->next = nB;

  nE->next = nA; //making cycle

  node = *nA;
}

void case1(Node &node){

  Node *nE = new Node();
  nE->data = 5;
  nE->next = NULL;

  Node *nD = new Node();
  nD->data = 4;
  nD->next = nE;

  Node *nC = new Node();
  nC->data = 3;
  nC->next = nD;

  Node *nB = new Node();
  nB->data = 2;
  nB->next = nC;

  Node *nA = new Node();
  nA->data = 1;
  nA->next = nB;

  nE->next = nB; //making cycle

  node = *nA;
}

void case2(Node &node){

  Node *nB = new Node();
  nB->data = 2;
  nB->next = NULL;

  Node *nA = new Node();
  nA->data = 1;
  nA->next = nB;

  node = *nA;
}

void case3(Node &node){

  Node *nA = new Node();
  nA->data = 1;
  nA->next = NULL;

  node = *nA;
}

void case4(Node &node){

  Node *nA = new Node();
  nA->data = 0;

  int N = 100;
  Node *new_node = new Node();
  new_node->data = 1;
  nA->next = new_node;
  for(int i=2; i <= N; i++) {
    Node * n = new Node();
    n->data = i;
    new_node->next = n;
    new_node = n;
  }

  new_node->next = nA->next;
  node = *nA;
}

bool has_cycle(Node* head){
  if (head != NULL) {
    Node* node;
    node = head->next;
    int count = 0;
    while (node != NULL){
      //printf("count:%d\n", count);
      if (node == head || node->next == head || count >= 100){
          return 1;
      }
      node = node->next;
      count += 1;
    }
    return 0;
  }
  return 0;
}

const char* bool_cast(const bool b){
  return b ? "true" : "false";
}

int main(){

cout << "Linked List" << endl;

Node node0;
case0(node0);
cout << "Case 0: has_link: " << bool_cast(has_cycle(&node0)) << endl;

Node node1;
case1(node1);
cout << "Case 1: has_link: " << bool_cast(has_cycle(&node1)) << endl;

Node node2;
case2(node2);
cout << "Case 2: has_link: " << bool_cast(has_cycle(&node2)) << endl;

Node node3;
case3(node3);
cout << "Case 3: has_link: " << bool_cast(has_cycle(&node3)) << endl;

Node node4;
case4(node4);
cout << "Case 4: has_link: " << bool_cast(has_cycle(&node4)) << endl;

}
