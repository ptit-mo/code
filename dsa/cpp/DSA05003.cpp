#include <bits/stdc++.h>
using namespace std;

int x, y, z;
string s1, s2, s3;

int qhd() {
	int C[x + 1][y + 1][z + 1];
	
	memset(C, 0, sizeof(C));
	
	for (int i = 1; i <= x; i++) {
		for (int j = 1; j <= y; j++) {
			for (int k = 1; k <= z; k++) {
				if (s1[i - 1] == s2[j - 1] && s1[i - 1] == s3[k - 1]) {
					C[i][j][k] = C[i - 1][j - 1][k - 1] + 1;
				}
				else {
					C[i][j][k] = max(C[i - 1][j][k], max(C[i][j - 1][k], C[i][j][k - 1]));
				}	
			}
		}
	}
	
	return C[x][y][z];
}

main() {
	int t;	cin >> t;
	while(t--) {
		cin >> x >> y >> z;
		cin >> s1 >> s2 >> s3;
		
		cout << qhd() << endl;
	}
}