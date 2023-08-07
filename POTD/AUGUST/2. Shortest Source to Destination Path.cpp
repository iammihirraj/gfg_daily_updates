// User function Template for C++
class Solution {
public:
    int shortestDistance(int N, int M, vector<vector<int>> A, int X, int Y) {
        if (A[0][0] == 0) {
            return -1;
        }

        vector<int> dx = {-1, 1, 0, 0};
        vector<int> dy = {0, 0, -1, 1};

        queue<pair<int, pair<int, int>>> q; // (x, (y, steps))

        A[0][0] = -1;

        q.push({0, {0, 0}}); // (x, (y, steps))

        while (!q.empty()) {
            int x = q.front().first;
            int y = q.front().second.first;
            int steps = q.front().second.second;
            q.pop();

            // Check if the target cell (X, Y) is reached
            if (x == X && y == Y) {
                return steps;
            }

            // Explore all four possible dir
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (nx >= 0 && nx < N && ny >= 0 && ny < M && A[nx][ny] == 1) {
                    q.push({nx, {ny, steps + 1}});

                    A[nx][ny] = -1;
                }
            }
        }

        // If the target cell (X, Y) is not reached, return -1
        return -1;
    }
};