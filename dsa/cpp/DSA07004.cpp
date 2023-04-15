#include <bits/stdc++.h>
using namespace std;
void xuly(string s){
    stack<char> st;  int count = 0,i;
    for(i = 0; i < s.length(); i++){
        if (s[i] != ')') st.push(s[i]);
        else{
            if (st.size() == 0){
                st.push('(');
                count++;
            }
            else st.pop();
        }
    }
    cout << count + st.size()/2 << endl;
}
main(){
    int t; string s;
    cin >> t;
    while(t--){
        string s; cin >> s;
		xuly(s);
    }
}