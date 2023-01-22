#include <bits/stdc++.h>
#define endl '\n'////
#define forn(i,n) for(int i=0;i<n;i++)
#define all(v)    v.begin(), v.end()
#define rall(v)   v.rbegin(),v.rend()
#define pb        push_back
#define sz(a)     (int)a.size()
#define pii       pair<int, int>
#define vi        vector<int>
typedef short sh;
typedef char ch;
typedef long long ll;
typedef double db;
typedef long double ld;

using namespace std;

const int INF = 987654321;
const int MM = 101;
bool visited[MM][MM];
int dx[4] = {0, 0, -1, 1};
int dy[4] = {1, -1, 0, 0};


void solve()
{
    memset(visited, 0, MM * MM);
    int n, m; cin >> n >> m;
    vector<int> mp[n];
    for(int i = 0; i < n; i++)
    {
        string input; cin >> input;
        for(int j = 0; j < input.size(); j++)
            mp[i].pb(input[j] - '0');
    }
    
    queue<pair<pair<int, int>, int>> q;
    q.push({{0, 0}, 1});
    visited[0][0] = true;

    while(!q.empty())
    {
        int cx = q.front().first.second;
        int cy = q.front().first.first;
        int cnt = q.front().second;
        if(cx == m - 1 & cy == n - 1)
        {
            cout << cnt << endl;
            break;
        }
        q.pop();
        for(int i = 0; i < 4; i++)
        {
            int nx = cx + dx[i];
            int ny = cy + dy[i];
            if(0 <= nx && nx < m && 0 <= ny && ny < n && !visited[ny][nx] && mp[ny][nx] == 1)
            {
                q.push({{ny, nx}, cnt + 1});
                visited[ny][nx] = true;
            }
        }
    }
}

int main()
{
    solve();
    return 0;
}