//10818 최소, 최대
#include <stdio.h>

int main(void){
    int n;
    scanf("%d", &n);

    int min=1000000, max=-1000000;
    for (int i=0;i<n;i++){
        int a;
        scanf("%d ",&a);
        if (min>a){
            min=a;
        }
        if (max<a){
            max=a;
        }
    }
    printf("%d %d",min,max);
    return 0;
}