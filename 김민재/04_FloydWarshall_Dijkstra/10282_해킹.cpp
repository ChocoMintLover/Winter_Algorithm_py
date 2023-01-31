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

const int INF = 999999999;
const int MM = 10001;
int dist[MM];

void dijkstra(int start, vector<pii> cp[])
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
        for(int i = 0; i < cp[cur].size(); i++)
        {
            int next = cp[cur][i].first;
            int next_dist = distance + cp[cur][i].second;
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
    int n, d, c;
    cin >> n >> d >> c;
    vector<pii> cp[n + 1];

    for(int i = 0; i < d; i++)
    {
        int a, b, cost;
        cin >> a >> b >> cost;
        cp[b].pb({a, cost});
    }
    for(int i = 0; i <= n; i++)
        dist[i] = INF;

    dijkstra(c, cp);
    //cnt = find_hacked_cp(c, cp);
    int ans = 0, cnt = 0;
    for(int i = 1; i <= n; i++)
        if(dist[i] != INF)
        {
            cnt++;
            ans = max(ans, dist[i]);
        }
    cout << cnt << ' ' << ans << endl;
}

int main()
{
    int t; cin >> t;
    while(t--)
        solve();
    return 0;
}