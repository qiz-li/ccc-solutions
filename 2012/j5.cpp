#include <iostream>
#include <queue>
#include <string>
#include <unordered_set>
#include <vector>
using namespace std;

string genKey(vector<vector<int>> pos)
{
    // Generate key by concatenating coin values
    // and seperating each postion with '-'
    string key = "";
    for (vector<int> i : pos)
    {
        key += '-';
        for (int j : i)
        {
            key += to_string(j);
        }
    }
    return key;
}

int solve(int n)
{
    // Generate 2D array of coin positions
    vector<vector<int>> vals(n);
    for (int i = 0; i < n; ++i)
    {
        int val;
        cin >> val;
        vals[i].push_back(val);
    }

    // Hash all visited states
    string key = genKey(vals);
    unordered_set<string> visited = {key};

    // Generate key target state
    string target;
    for (int i = 1; i <= n; ++i)
    {
        target += '-';
        target += to_string(i);
    }

    // BFS all possible states
    queue<pair<vector<vector<int>>, int>> q;
    q.push({vals, 0});
    while (!q.empty())
    {
        pair<vector<vector<int>>, int> cur = q.front();
        q.pop();
        int step = cur.second;
        vector<vector<int>> pos = cur.first;

        // Reached target state
        string key = genKey(pos);
        if (key == target)
        {
            cout << step << '\n';
            return 0;
        }

        // Go through all positions
        for (int i = 0; i < n; ++i)
        {
            // Up/down
            for (int j = i - 1; j <= i + 1; j += 2)
            {
                // Check if coin can be move up/down
                if (0 <= j and j <= n - 1 and !cur.first[i].empty() and
                    (cur.first[j].empty() or
                     cur.first[j].back() > cur.first[i].back()))
                {
                    // Simulate coin move
                    vector<vector<int>> nPos = cur.first;
                    nPos[j].push_back(nPos[i].back());
                    nPos[i].pop_back();
                    string nKey = genKey(nPos);
                    if (visited.find(nKey) == visited.end())
                    {
                        visited.insert(nKey);
                        q.push({nPos, step + 1});
                    }
                }
            }
        }
    }
    cout << "IMPOSSIBLE" << '\n';
    return 0;
}

int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;
    while (n != 0)
    {
        solve(n);
        cin >> n;
    }
}