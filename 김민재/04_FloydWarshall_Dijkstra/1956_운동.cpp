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

void floydWarshall(int m[][MM], int dist[][MM])
{
    for(int k = 0; k < MM; k++)
    {
        for(int i = 0; i < MM; i++)
        {
            for(int j = 0; j < MM; j++)
            {
                if(dist[i][k] != INF && dist[k][j] != INF)
                {
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }
    }
}

void solve()
{
    int v, e;
    cin >> v >> e;

    int m[MM][MM];
    int dist[MM][MM];

    forn(i, MM)
        forn(j, MM)
            m[i][j] = INF;

    for(int i = 0; i < e; i++)
    {
        int a, b, c;
        cin >> a >> b >> c;
        m[a][b] = c;
    }
    
    for(int i = 0; i < MM; i++)
        for(int j = 0; j < MM; j++)
            dist[i][j] = m[i][j];

    floydWarshall(m, dist);

    int mm_dist = INF;
    for(int i = 1; i < MM; i++)
    {
        for(int j = 1; j < MM; j++)
        {
            mm_dist = min(mm_dist, dist[i][j] + dist[j][i]);
        }
    }
    if(mm_dist >= INF)
        cout << "-1" << endl;
    else
        cout << mm_dist << endl;
}

int main()
{
    solve();
    return 0;
}