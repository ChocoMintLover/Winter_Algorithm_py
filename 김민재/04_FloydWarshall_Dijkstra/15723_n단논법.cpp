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

void floydWarshall(int dist[27][27], int a[27][27])
{
    for(int i = 0; i < 27; i++)
        for(int j = 0; j < 27; j++)
            dist[i][j] = a[i][j];

    for(int k = 0; k < 27; k++)
        for(int i = 0; i < 27; i++)
            for(int j = 0; j < 27; j++)
            {
                if(dist[i][k] && dist[k][j])
                    dist[i][j] = 1;
            }
}

void solve()
{
    int n, m; cin >> n;
    cin.ignore();
    int a[27][27];
    int dist[27][27];

    for(int i = 0; i < 27; i++)
        for(int j = 0; j < 27; j++)
            a[i][j] = 0;


    for(int i = 0; i < n; i++)
    {
        string propo;
        getline(cin, propo);
        a[propo.front() - 'a'][propo.back() - 'a'] = 1;
    }
    
    floydWarshall(dist, a);

    cin >> m;
    cin.ignore();
    for(int i = 0; i < m; i++)
    {
        string conclu;
        getline(cin, conclu);
        if(dist[conclu.front() - 'a'][conclu.back() - 'a'] == 1)
            cout << 'T' << endl;
        else
            cout << 'F' << endl;
    }
}

int main()
{
    solve();
    return 0;
}