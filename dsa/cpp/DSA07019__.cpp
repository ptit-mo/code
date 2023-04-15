#include <bits/stdc++.h>
using namespace std;
main(){
    int t,n,i; cin >> t;
    while(t--){
        cin >> n;
        long long H[n], L[n], R[n];
        for(i = 0; i < n; i++) cin >> H[i];
        stack<int> st;
		
        st.push(-1); 
        for (i = 0; i < n; i++){
            while (st.size() > 1 && H[st.top()] >= H[i]) st.pop();
            L[i] = st.top() + 1;
            st.push(i);
        }
        while(!st.empty()) st.pop();
		
        st.push(n);
        for (i = n - 1; i >= 0; i--){
            while(st.size() > 1 && H[st.top()] >= H[i]) st.pop();
            R[i] = st.top() - 1;
            st.push(i);
        }
		
        long long res = 0;
        for (i = 0; i < n; i++)
			res = max(res, (R[i] - L[i] + 1) * H[i]);
        cout << res << endl;
    }
}