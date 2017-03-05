#include <cstdlib>
#include <cassert>

struct Node {
   int data;
   Node* left;
   Node* right;
};

bool checkLesser(Node* node, int value){
    if (node == NULL){
        return true;
    }
    if ((node->data < value) && (checkLesser(node->left, value)) && checkLesser(node->right, value)){
        return true;
    }
    return false;
 }

 bool checkGreater(Node* node, int value){
    if (node == NULL){
        return true;
    }
    if ((node->data > value) && (checkGreater(node->left, value)) && checkGreater(node->right, value)){
        return true;
    }
    return false;
 }

 bool checkBST(Node* root) {

     if (root == NULL){
         return true;
     }
     if ( checkLesser(root->left, root->data) && checkGreater(root->right, root->data) && checkBST(root->left) && checkBST(root->right) ){
         return true;
     }
     return false;
 }

void initialize(Node& n, int value){
  Node * node = new Node();
  node->data = value;
  node->left = NULL;
  node->right = NULL;
  n = *node;
}

void case0(){
  Node no8;
  initialize(no8, 8);

  Node no6;
  initialize(no6, 6);
  Node no4;
  initialize(no4, 4);

  no6.left = &no4;
  no8.left = &no6;

  assert(checkBST(&no8) == true);
}

void case1(){
  Node no10;
  initialize(no10, 10);
  Node no5;
  initialize(no5, 5);

  no10.left = &no5;
  Node no4;
  initialize(no4, 5);
  Node no1;
  initialize(no1, 1);
  no5.left = &no4;
  no4.left = &no1;

  Node no7;
  initialize(no7, 7);
  no5.right = &no7;

  Node no11;
  initialize(no11, 11);
  no5.right = &no11;

  Node no16;
  initialize(no16, 16);
  no10.right = &no16;

  assert(checkBST(&no10) == false);
}

int main(){
  case0();
}
