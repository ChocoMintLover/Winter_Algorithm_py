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
const int MM = 102;
bool visited[MM];
bool is_find = false;
int n;
pii destination;

int len_btw(vector<pii> &e, int a, int b)
{
    int res = (int)abs(e[a].first - e[b].first) + (int)abs(e[a].second - e[b].second);
    return res;
}

void dfs(vector<pii> &e, int idx)
{
    if(idx == n + 1)
    {
        cout << "happy" << endl;
        is_find = true;
        return;
    }
    visited[idx] = true;
    for(int i = 0; i < e.size(); i++)
    {
        if(!visited[i] && len_btw(e, idx, i) <= 1000)
        {
            dfs(e, i);
            if(is_find) return;
        }
    }
}

void solve()
{
    is_find = false;
    memset(visited, 0, MM);
    cin >> n;
    vector<pii> e;

    for(int i = 0; i < n + 2; i++)
    {
        int x, y; cin >> x >> y;
        e.pb({x, y});
    }
    destination = {e.back().first, e.back().second};
    dfs(e, 0);
    if(!is_find)
        cout << "sad" << endl;
}

int main()
{
    int t; cin >> t;
    while(t--)
        solve();
    return 0;
}