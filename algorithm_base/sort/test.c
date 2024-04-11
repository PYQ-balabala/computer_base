#include<stdio.h>
/*
冒泡排序
*/
void bulubulu(int a[], int len){
int i = 0;
int j = 0;
int tmp;
for(i=0; i < len; i++){
    for(j = i + 1; j < len; j++){
        if(a[j] < a[i]){
            tmp = a[i];
            a[i] = a[j];
            a[j] = tmp;
        }
    }
}
}

int main(){
    int a[] = {5, 4, 3, 2, 1};
    bulubulu(a, 5);
    for(int i = 0; i < 5; i++){
        printf("%d ", a[i]);
    }
    printf("\n");
    return 0;
}