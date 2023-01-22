#include <bits/stdc++.h>
#define endl '\n'
#define forn(i,n) for(int i=0;i<n;i++)
#define all(v)    v.begin(), v.end()
#define rall(v)   v.rbegin(),v.rend()
#define pb        push_back
#define sz(a)     (int)a.size()
#define pii       pair<int, int>
#define myinput int input; cin >> input;
typedef short sh;
typedef char ch;
typedef long long ll;
typedef double db;
typedef long double ld;

using namespace std;
const int MM = 101;
bool visited[MM];
bool fam_find = false;
set<int> fam[MM];
int s, e;

void dfs(int val, int dep)
{
    if(val == e)
    {
        fam_find = true;
        cout << dep << endl;
        return;
    }

    if(visited[val])
        return;
    visited[val] = true;
    for(auto m : fam[val])
    {
        if(!visited[m])
            dfs(m, dep + 1);
    }
}

void solve()
{
    int n, m;
    cin >> n >> s >> e >> m;

    for(int i = 0; i < m; i++)
    {
        int p, c; cin >> p >> c;
        fam[p].insert(c);
        fam[c].insert(p);
    }

    dfs(s, 0);
    if(!fam_find)
        cout << "-1" << endl;

}

int main()
{
    solve();

    return 0;
}