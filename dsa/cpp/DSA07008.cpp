#include<bits/stdc++.h>
using namespace std;
int uutien(char c){
    if(c=='+' || c=='-') return 1;
    if(c=='*' || c=='/') return 2;
    if(c == '^') return 3;
    return -1;
}
void xuly(string s){
    stack<char> st; int i,j;
    string kq="";
    for(i=0;i<s.length();i++){
        if(isalpha(s[i])) kq += s[i];
        else if(s[i]=='(') st.push(s[i]);
        else if(s[i]==')'){
            while(!st.empty() && st.top()!='('){
                 char c = st.top(); st.pop();
                 kq += c;
            }
            if(st.top()=='(') st.pop();
        } else {
            while(!st.empty() && uutien(s[i]) <= uutien(st.top())){
                 char c = st.top(); st.pop();
                 kq += c;
            }
            st.push(s[i]);
        }
    }
    while(!st.empty() && st.top()!='('){
        char c = st.top(); st.pop();
        kq += c;
    }
    cout << kq << endl;
}
main(){
    int t; string s;
    cin >> t; cin.ignore();
    while(t--){
        cin >> s;
        xuly(s);
    }
}
