#include <iostream>
#include <cstdio>
using namespace std;


int max_of_four(int a, int b, int c, int d){
    int maxval;
    if(a>b){
        if(a>c){
            if(a>d)
               maxval=a; 
            
            else
                maxval=d;
            }
        else{
            if(c>d)
                maxval=c;
            else 
                maxval=d;
            }
    }
    else{
        if(b>c){
            if(b>d){
                maxval=b;
                }
            else{
                maxval=d;
            }
        }
        else{
            if(c>d){
                maxval=c;
                
            }
            else
                maxval=d;
        }
    }
    return maxval;
}
        
        
        
    


int main() {
    int a, b, c, d;
    
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}

