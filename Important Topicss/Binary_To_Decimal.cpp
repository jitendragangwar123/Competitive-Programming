#include <bits/stdc++.h>  // This will work only for g++ compiler. 
using namespace std;
class Solution{
public:
    int binary_to_decimal(string str){
        //reverse the string
        reverse(str.begin(),str.end());
    	int sum=0;
    	for(int i=0;i<str.length();i++){
        	if(str[i]=='1'){
        		sum+=pow(2,i);
        	}
        }	      
      return sum;
    }	  
};		
    		 

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int t;
    cin>>t;
    while(t--){
        string str;
        cin>>str;
        Solution ob;
        cout<<ob.binary_to_decimal(str);
        
    }
  return 0;
}
