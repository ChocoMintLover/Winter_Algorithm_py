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
const int MM = 401;

void floydWarshall(int m[][MM], int dist[][MM], int n)
{
    for(int k = 1; k <= n; k++)
        for(int i = 1; i <= n; i++)
            for(int j = 1; j <= n; j++)
                if(dist[i][k] == 1 && dist[k][j] == 1)
                    dist[i][j] = 1;
}

void solve()
{
    int n, k;
    cin >> n >> k;

    int m[MM][MM];
    int dist[MM][MM];

    forn(i, MM)
        forn(j, MM)
            m[i][j] = 0;

    for(int i = 0; i < k; i++)
    {
        int a, b;
        cin >> a >> b;
        m[a][b] = 1;
    }
    
    for(int i = 0; i < MM; i++)
        for(int j = 0; j < MM; j++)
            dist[i][j] = m[i][j];

    floydWarshall(m, dist, n);

    int s; cin >> s;
    for(int i = 0; i < s; i++)
    {
        int a, b;
        cin >> a >> b;
        if(dist[a][b] == 1)
        {
            cout << "-1";
        }
        else if (dist[a][b] == 0)
        {
            if(dist[b][a] == 1)
                cout << '1';
            else if(dist[b][a] == 0)
                cout << '0';
        }
        cout << endl;
    }
}

int main()
{
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    solve();
    return 0;
}