/*Question:-
##You are given an array representing the heights of neighboring buildings on a city street, 
from east to west. The city assessor would like you to write an algorithm that returns how many of 
these buildings have a view of the setting sun, in order to properly value the street.
For example, given the array [3, 7, 8, 3, 6, 1], you should return 3, since the top floors of the 
buildings with heights 8, 6, and 1 all have an unobstructed view to the west.
Can you do this using just one forward pass through the array?*/


#include <bits/stdc++.h>  // This will work only for g++ compiler. 
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        int arr[n];
        for(int i=0;i<n;i++){
            cin>>arr[i];
        }
        int count=0;
        int c_max=INT_MIN;
        for(int i=0;i<n;i++){
            if(arr[i]>=c_max){
                count+=1;
                c_max=arr[i];
            }
        }
        cout<<count<<"\n";
    }
  return 0;
}
