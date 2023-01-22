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

void floydWarshall(int a[101][101], int n)
{
    int dist[n][n];
    for(int i = 0; i < n; i++)
        for(int j = 0; j < n; j++)
            dist[i][j] = a[i][j];

    for(int k = 0; k < n; k++)
        for(int i = 0; i < n; i++)
            for(int j = 0; j < n; j++)
            {
                if(dist[i][k] + dist[k][j] < dist[i][j])
                    dist[i][j] = dist[i][k] + dist[k][j];
            }

    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < n; j++)
        {
            if(dist[i][j] < INF)
                cout << "1 ";
            else    
                cout << "0 ";
        }    
        cout << endl;
    }
}

void solve()
{
    int n; cin >> n;
    int m[101][101];
    for(int i = 0; i < n; i++)
        for(int j = 0; j < n; j++)
        {
            cin >> m[i][j];
            if(m[i][j] == 0)
                m[i][j] = INF;
        }
    
    floydWarshall(m, n);

}

int main()
{
    solve();
    return 0;
}