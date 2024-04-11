#include<stdio.h>
#include<stdlib.h>

int *array_insert(int src[], int len, int index, int content){
    int *p = (int *)malloc((len + 1) * sizeof(int));
    for (int i = 0; i < index; i++){
        p[i] = src[i];
    }
    p[index] = content;
    for (int i = index + 1; i < len + 1; i++){
        p[i] = src[i-1];
    }
    return p;
}

int *array_delete(int src[], int len, int index){
    int *p = (int *)malloc((len - 1) * sizeof(int));
    for (int i = 0; i < index; i++){
        p[i] = src[i];
    }
    for (int i = index + 1; i < len; i++){
        p[i - 1] = src[i]; 
    }
    return p;
}

int main(){
    int a[] = {1, 2, 3, 4, 5};
    int *tmp = array_delete(a, 5, 3);
    for (int i = 0; i < 4; i++){
        printf("%d ", tmp[i]);
    }
    printf("\n");
    return 0;
}