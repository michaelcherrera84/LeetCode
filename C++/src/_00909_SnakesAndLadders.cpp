#include <vector>
#include <queue>
#include <unordered_set>
#include <utility>

class Solution
{
public:
    int snakesAndLadders(std::vector<std::vector<int>> &board)
    {
        int n = board.size();
        std::queue<std::pair<int, int>> queue;
        std::unordered_set<int> visited;

        queue.push({1, 0});
        visited.insert(1);

        while (!queue.empty())
        {
            auto [pos, rolls] = queue.front();
            queue.pop();

            for (int i = 1; i <= 6; i++)
            {
                int next = pos + i;

                if (next > n * n)
                    break;

                auto [r, c] = getIndices(next, n);

                if (board[r][c] != -1)
                    next = board[r][c];

                if (next == n * n)
                    return rolls + 1;

                if (!visited.count(next))
                {
                    visited.insert(next);
                    queue.push({next, rolls + 1});
                }
            }
        }

        return -1;
    }

private:
    std::pair<int, int> getIndices(int pos, int n) const
    {
        int r = (pos - 1) / n;
        int c = (pos - 1) % n;

        int row = n - 1 - r;
        int col = r % 2 == 0 ? c : n - 1 - c;

        return {row, col};
    }
};