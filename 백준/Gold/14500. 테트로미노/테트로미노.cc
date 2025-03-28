#include <iostream>
#include <vector>
using namespace std;

int n, m;
vector<vector<int>> board;
int answer = 0;

// Tetris shapes (same coordinates as in your Python code)
vector<vector<pair<int, int>>> tetris = {
    {{0, 0}, {0, 1}, {1, 0}, {1, 1}},  // square
    {{0, 0}, {0, 1}, {0, 2}, {0, 3}},  // I horizontal
    {{0, 0}, {1, 0}, {2, 0}, {3, 0}},  // I vertical
    {{0, 0}, {1, 0}, {1, 1}, {2, 1}},  // Z
    {{1, 0}, {0, 1}, {1, 1}, {2, 0}},  // Z rotated
    {{1, 0}, {1, 1}, {0, 1}, {0, 2}},  
    {{0, 0}, {0, 1}, {1, 1}, {1, 2}},
    {{0, 0}, {1, 0}, {2, 0}, {2, 1}},  // L
    {{0, 1}, {1, 1}, {2, 0}, {2, 1}},
    {{0, 0}, {0, 1}, {1, 0}, {2, 0}},
    {{0, 0}, {0, 1}, {1, 1}, {2, 1}},
    {{1, 0}, {0, 1}, {1, 1}, {1, 2}},
    {{0, 0}, {0, 1}, {0, 2}, {1, 1}},
    {{0, 0}, {1, 0}, {1, 1}, {1, 2}},
    {{1, 0}, {1, 1}, {1, 2}, {0, 2}},
    {{0, 0}, {0, 1}, {0, 2}, {1, 0}},
    {{0, 0}, {0, 1}, {0, 2}, {1, 2}},
    {{0, 0}, {1, 0}, {1, 1}, {2, 0}},
    {{1, 0}, {0, 1}, {1, 1}, {2, 1}}   // T
};

void solution(int x, int y) {
    for(int i = 0; i < 19; i++) {
        int tmp = 0;
        bool valid = true;
        
        for(int j = 0; j < 4; j++) {
            int nx = x + tetris[i][j].first;
            int ny = y + tetris[i][j].second;
            
            if(nx < 0 || nx >= n || ny < 0 || ny >= m) {
                valid = false;
                break;
            }
            
            tmp += board[nx][ny];
        }
        
        if(valid) {
            answer = max(answer, tmp);
        }
    }
}

int main() {
    // Input
    cin >> n >> m;
    board.resize(n, vector<int>(m));
    
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            cin >> board[i][j];
        }
    }
    
    // Process each position
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            solution(i, j);
        }
    }
    
    // Output
    cout << answer << endl;
    
    return 0;
}