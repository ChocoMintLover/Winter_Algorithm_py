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
const int MM = 801;
int dist[MM];

void dijkstra(int start, vector<pii> nd[])
{
    dist[start] = 0;
    priority_queue<pii> pq;
    pq.push({start, 0});

    while(!pq.empty())
    {
        int cur = pq.top().first;
        int distance = -pq.top().second;
        pq.pop();
        if(dist[cur] < distance) continue;
        for(int i = 0; i < nd[cur].size(); i++)
        {
            int next = nd[cur][i].first;
            int next_dist = distance + nd[cur][i].second;
            if(next_dist < dist[next])
            {
                dist[next] = next_dist;
                pq.push({next, -next_dist});
            }
        }
    }
}

void solve()
{
    int n, e;
    cin >> n >> e;
    vector<pii> nd[n + 1];

    for(int i = 0; i < e; i++)
    {
        int a, b, cost;
        cin >> a >> b >> cost;
        nd[a].pb({b, cost});
        nd[b].pb({a, cost});
    }
    int v1, v2;
    cin >> v1 >> v2;

    ll ans1 = 0, ans2 = 0;
    for(int i = 1; i <= n; i++)
        dist[i] = INF;
    dijkstra(1, nd);
    ans1 += dist[v1];
    ans2 += dist[v2];
    for(int i = 1; i <= n; i++)
    dist[i] = INF;
    dijkstra(v1, nd);
    ans1 += dist[v2];
    ans2 += dist[v2] + dist[n];
    for(int i = 1; i <= n; i++)
        dist[i] = INF;
    dijkstra(v2, nd);
    ans1 += dist[n];

    ll ans = min(ans1, ans2);
    if(ans >= INF)
        cout << "-1" << endl;
    else    
        cout << ans << endl;
}

int main()
{
    solve();
    return 0;
}