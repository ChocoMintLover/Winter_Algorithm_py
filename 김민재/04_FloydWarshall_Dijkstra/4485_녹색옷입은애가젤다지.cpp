#include <bits/stdc++.h>
#define endl '\n'
#define forn(i,n) for(int i=0;i<n;i++)
#define all(v)    v.begin(), v.end()
#define rall(v)   v.rbegin(),v.rend()
#define pb        push_back
#define sz(a)     (int)a.size()
#define pii       pair<int, int>
#define vi		  vector<int>
typedef short sh;
typedef char ch;
typedef long long ll;
typedef double db;
typedef long double ld;

using namespace std;

const int INF = 999999999;
const int MM = 126;
int cnt_problem = 1;
int n;
int dist[MM][MM];
int e[MM][MM];
int dx[4] = {0, -1, 0, 1};
int dy[4] = {-1, 0, 1, 0};


void dijkstra()
{
	dist[0][0] = e[0][0];
	// cost, y, x
	priority_queue<pair<int, pii>> pq;
	pq.push({-e[0][0], {0, 0}});

	while(!pq.empty())
	{
		int y = pq.top().second.first;
		int x = pq.top().second.second;
		int cost = -pq.top().first;
		pq.pop();

		for(int i = 0; i < 4; i++)
		{
			int ny = y + dy[i];
			int nx = x + dx[i];
			
			if(0 <= nx && nx < n && 0 <= ny && ny < n)
			{
				int new_cost = cost + e[ny][nx];
				if(dist[ny][nx] > new_cost)
				{
					dist[ny][nx] = new_cost;
					pq.push({-dist[ny][nx], {ny, nx}});
				}

			}
		}
	}
}

void solve(int n)
{
	for(int i = 0; i < n; i++)
		for(int j = 0; j < n; j++)
			dist[i][j] = INF;
	for(int i = 0; i < n; i++)
		for(int j = 0; j < n; j++)
			cin >> e[i][j];
	dijkstra();
	cout << "Problem "<< cnt_problem << ": "<< dist[n - 1][n - 1] << endl;
	cnt_problem++;
}

int main()
{
	while(1)
	{
		cin >> n;
		if(n != 0)
    		solve(n);
		else
			break;
	}
    return 0;
}