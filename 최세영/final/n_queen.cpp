#include <iostream>
#include <string>
#include <cmath>
#include <algorithm>
#include <vector>

using namespace std;
int counts = 0;
int N;
int arr[15];

bool possible(int row) {
	for(int i = 0; i < row; i++) {
		if(arr[row] == arr[i] || row - i == abs(arr[row] - arr[i])) {
			return false;
		}
	}
	return true;
}

void setQueen(int row) {
	if(row == N) {
		counts++;
	}
	else {
		for(int i = 0; i < N; i++) {
			arr[row] = i + 1;
			if(possible(row)) {
				
				setQueen(row + 1);
			}
		}
	}
}


int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	
    cin>>N;

	setQueen(0);
	cout << counts << endl;
    return 0;
}