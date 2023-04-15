#include<bits/stdc++.h>
using namespace std;
int kiemtra(string s){
    int n = s.length();  stack<char> st;
    for(int i=0;i<n;i++){
        if(s[i]=='(' || s[i] =='[' || s[i] == '{') 
			st.push(s[i]);
        else {
            if(st.empty()) return 0;
            char in = st.top(), out = s[i];
            if(in == '(' && out == ')') st.pop();
            else if(in == '[' && out == ']') st.pop();
            else if(in == '{' && out == '}') st.pop();
            return 0;
        }
    }
    return st.empty();
}
main(){
    int t; cin >> t;
    while(t--){
        string s; cin >> s;
        if(kiemtra(s)) cout << "YES" << endl;
        else cout << "NO" << endl;
    }
}

