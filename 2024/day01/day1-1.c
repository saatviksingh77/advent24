#include<stdio.h>
#define N 1000
int main(){
    int a[N],b[N];
    for(int i=0;i<N;i++) scanf("%d %d",&a[i],&b[i]);
    int changed=1,temp=0;
    while(changed){
        changed=0;
        for(int i=0;i<N-1;i++){
            if(a[i]>a[i+1]){
                changed=1;
                temp=a[i];
                a[i]=a[i+1];
                a[i+1]=temp;
            }
        }
    }
    changed=1,temp=0;
    while(changed){
        changed=0;
        for(int i=0;i<N-1;i++){
            if(b[i]>b[i+1]){
                changed=1;
                temp=b[i];
                b[i]=b[i+1];
                b[i+1]=temp;
            }
        }
    }
    int sum=0;
    for(int i=0;i<N;i++) sum+=a[i]-b[i]>0?a[i]-b[i]:b[i]-a[i];
    printf("%d",sum);
    return 0;
}