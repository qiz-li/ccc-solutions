#include <vector>
#include <queue>
#include <string>
#include <iostream>
#include <unordered_map>
using namespace std;

bool searched[1001][1001];
int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);

    unordered_map<int, vector<pair<int, int>>> vals;
    int m, n;
    cin >> m >> n;

    for (int row = 1; row <= m; ++row)
    {
        for (int col = 1; col <= n; ++col)
        {
            int val;
            cin >> val;
            searched[row][col] = false;
            vals[val].push_back({row, col});
        }
    }

    queue<pair<int, int>> q;
    q.push({m, n});
    while (!q.empty())
    {
        pair<int, int> cur = q.front();
        q.pop();
        int product = cur.first * cur.second;
        if (vals.find(product) != vals.end())
        {
            vector<pair<int, int>> &pairs = vals[product];
            for (pair<int, int> i : pairs)
            {
                if (i.first == 1 && i.second == 1)
                {
                    cout << "yes" << '\n';
                    return 0;
                }
                else if (!searched[i.first][i.second])
                {
                    searched[i.first][i.second] = true;
                    q.push(i);
                }
            }
        }
    }
    cout << "no" << '\n';
    return 0;
}