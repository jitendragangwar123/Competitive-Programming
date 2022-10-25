#include <bits/stdc++.h>  
using namespace std;
class Solution{
    public:
    // Function to check if given number n is a power of two.
    bool isPowerofTwo(long long n){
        
        // Your code here 
        if(n<=0){
            return false;
        }
        else{
            //return ((n&(n-1))==0);
            return ceil(log2(n))==floor(log2(n));
        }
   }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    int t;
    cin>>t;
    while(t--){
      long long n;
      cin>>n;
      Solution ob;
      if(ob.isPowerofTwo(n)){
          cout<<"YES"<<endl;
      }
      else{
          cout<<"No"<<endl;
      }
  }
  return 0;
}
