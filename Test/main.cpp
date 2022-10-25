// file i/o for comptitive programming

#include<iostream>
using namespace std;
int main(){
    #ifndef ONLINE_JUDGE
       freopen("input.txt","r",stdin);
       freopen("output.txt","w",stdout);
    #endif
    // Enter the test case
    int test;
    cin>>test;
    for(int i=0;i<test;i++){
        int a,b;
        cin>>a>>b;
        cout<<a+b<<'\n';
    }
    return 0;
    }   
