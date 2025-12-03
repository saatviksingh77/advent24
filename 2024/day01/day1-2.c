#include<stdio.h>
#define N 1000
int main(){
    int a[N][2],b[N];
    for(int i=0;i<N;i++) scanf("%d %d",&a[i][0],&b[i]);
    int count=0;
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            if(a[i][0]==b[j]) count++;
        }
        a[i][1]=count;
        count=0;
    }
    int sum=0;
    for(int i=0;i<N;i++) sum+=a[i][0]*a[i][1];
    printf("%d",sum);
    return 0;
}