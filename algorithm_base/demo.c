#include<stdio.h>
int mod(int a, int b){
    return a % b;
}

int add(int a, int b){
    int res = mod(a, b);
    return res + b;
}

void main(){
    int a = 2;
    int b = 3;
    int c = add(a, b);
}